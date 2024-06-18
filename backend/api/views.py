from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from .models import *
from .serializers import *

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        category_id = data.get('category_id')

        # Fetch the Category instance
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new Programmer entry
        programmer = Programmer.objects.create(
            name=data['name'],
            email=data['email'],
            password=data['password'],
            phone_number=data.get('phone_number', None),
            address=data.get('address', None),
            experience=data['experience'],
            rate=data['rate'],
            categories=category,
            skills=data['skills'],
            bio=data['bio'],
            profile_picture=data.get('profile_picture', None),
            cv=data.get('cv', None)
        )

        # Create the specific category-based model
        category_name = category.name.lower()
        if category_name == 'webdeveloper':
            WebDeveloper.objects.create(programmer=programmer)
        elif category_name == 'backenddeveloper':
            BackEndDeveloper.objects.create(programmer=programmer)
        elif category_name == 'networking':
            Networking.objects.create(programmer=programmer)
        elif category_name == 'ai/machinelearning':
            MachineLearning.objects.create(programmer=programmer)
        elif category_name == 'cloudservices':
            CloudServices.objects.create(programmer=programmer)
        elif category_name == 'admincustomersupport':
            AdminCustomerSupport.objects.create(programmer=programmer)

        return Response(ProgrammerSerializer(programmer).data, status=status.HTTP_201_CREATED)

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RegisterProgrammerView(generics.CreateAPIView):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer

class RegisterClientView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ObtainTokenPairWithEmailView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)