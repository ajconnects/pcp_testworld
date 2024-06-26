from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from .models import *
from .serializer import *
import jwt, datetime
from django.contrib.auth import authenticate
from django.core.mail import send_mail

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()  # Convert QueryDict to a regular dictionary to make it mutable

        # Extract and handle user data
        user_data = {
            'name': data.get('user.name'),
            'email': data.get('user.email'),
            'password': data.get('user.password')
        }

        if not user_data['name'] or not user_data['email'] or not user_data['password']:
            return Response({"error": "'name', 'email', and 'password' are required in 'user' data"}, status=status.HTTP_400_BAD_REQUEST)

        data['user'] = user_data

        # Handle the optional profile picture
        if 'profile_picture' in request.FILES:
            data['profile_picture'] = request.FILES['profile_picture']

        programmer_serializer = self.get_serializer(data=data)
        programmer_serializer.is_valid(raise_exception=True)
        programmer = programmer_serializer.save()

        # Handle category association
        category_id = data.get('category_id')
        if category_id:
            try:
                category = Category.objects.get(pk=category_id)
                programmer.categories = category
                programmer.save()
            except Category.DoesNotExist:
                return Response({"error": "Category not found"}, status=status.HTTP_400_BAD_REQUEST)

        # Include the ID in the response
        response_data = programmer_serializer.data
        response_data['id'] = programmer.id

        return Response(response_data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = request.data.copy()

        # Extract and handle user data
        user_data = {
            'name': data.get('user.name', instance.user.name),
            'email': data.get('user.email', instance.user.email)
        }

        if 'user.password' in data:
            user_data['password'] = data.get('user.password')

        data['user'] = user_data

        # Handle the optional profile picture
        if 'profile_picture' in request.FILES:
            data['profile_picture'] = request.FILES['profile_picture']

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        programmer = serializer.save()

        # Handle category association
        category_id = data.get('category_id')
        if category_id:
            try:
                category = Category.objects.get(pk=category_id)
                programmer.categories = category
                programmer.save()
            except Category.DoesNotExist:
                return Response({"error": "Category not found"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        category_id = request.query_params.get('category')
        if category_id:
            self.queryset = self.queryset.filter(categories__id=category_id)
        return super().list(request, *args, **kwargs)

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()  # Convert QueryDict to a regular dictionary to make it mutable

        # Extract and handle user data
        user_data = {
            'name': data.get('user.name'),
            'email': data.get('user.email'),
            'password': data.get('user.password')
        }

        if not user_data['name'] or not user_data['email'] or not user_data['password']:
            return Response({"error": "'name', 'email', and 'password' are required in 'user' data"}, status=status.HTTP_400_BAD_REQUEST)

        data['user'] = user_data

        # Handle the optional profile picture
        if 'profile_picture' in request.FILES:
            data['profile_picture'] = request.FILES['profile_picture']

        client_serializer = self.get_serializer(data=data)
        client_serializer.is_valid(raise_exception=True)
        client = client_serializer.save()

        # Include the ID in the response
        response_data = client_serializer.data
        response_data['id'] = client.id

        return Response(response_data, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = authenticate(request, username=email, password=password)

        if user is None:
            raise AuthenticationFailed('Please enter a correct email and password. Note that both fields may be case-sensitive.')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        # Determine if the user is a programmer or a client
        try:
            programmer = Programmer.objects.get(user=user)
            user_type = 'programmer'
            user_id = programmer.id
        except Programmer.DoesNotExist:
            try:
                client = Client.objects.get(user=user)
                user_type = 'client'
                user_id = client.id
            except Client.DoesNotExist:
                raise AuthenticationFailed('User type not found.')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token,
            'user_type': user_type,
            'user_id': user_id
        }

        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {'message': 'success logout'}
        return response

class PublicProgrammerSearchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        query = request.query_params.get('q', '')
        if query:
            programmers = Programmer.objects.filter(skills__icontains=query).select_related('user', 'categories')
            serializer = PublicProgrammerSerializer(programmers, many=True)
            return Response(serializer.data)
        return Response({"message": "No search query provided."}, status=400)
