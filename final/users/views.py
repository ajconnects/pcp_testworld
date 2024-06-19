from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, APIException
from rest_framework.authentication import get_authorization_header
import jwt, datetime
from .serializers import UserSerializer
from .models import User
from .authenication import create_access_token, create_refresh_token, decode_refresh_token, decode_access_token

#user register
class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# #user login  PART 1 other way with access and refresh token
# class LoginView(APIView):
#     def post(self, request):
#         email = request.data['email']
#         password = request.data['password']

#         user = User.objects.filter(email=email).first()

#         if user is None:
#             raise AuthenticationFailed('User not found!')
#         #using the check password the because is hash
#         if not user.check_password(password):
#             raise AuthenticationFailed('Incorrect password!')


#         #using the jwt i have to install PyJWT
#         payload = {
#             'id': user.id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),  #how long the token will last
#             'iat': datetime.datetime.utcnow() #when token is created
#         }

#         token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

#         response = Response()

#         #setting cookie
#         response.set_cookie(key='jwt', value=token, httponly=True) #httponly for the backend

#         response.data = { 'jwt': token }

#         return response

#User Login PART 2 But link to the authentication.py using access and refresh token
class LoginView(APIView):
    def post(self, request):

        user = User.objects.filter(email=request.data['email']).first()

        if user is None:
            raise APIException('User not found!')

        if not user.check_password(request.data['password']):
            raise APIException('Incorrect password!')

        access_token = create_access_token(user.id) #as serializer
        refresh_token = create_refresh_token(user.id) #as cookies

        response = Response()

        response.set_cookie(key='refreshToken', value=refresh_token, httponly=True)
        response.data = {
            'token': access_token
        }

        return response


# #user authenticate part 1 other method in part 2
# class UserView(APIView):
#     def get(self, request):
#         token = request.COOKIES.get('jwt')

#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')

#         try:
#             payload = jwt.decode(token, 'secret', algorithms=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated Error!')

#         user = User.objects.filter(id=payload['id']).first()
#         serializer = UserSerializer(user)

#         return Response(serializer.data)


#user authenticate path 2 with login
class UserView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')  #access token
            id = decode_access_token(token)

            user = User.objects.filter(pk=id).first()

            return Response(UserSerializer(user).data)

        raise AuthenticationFailed('unauthenticated error!')

#user refresh for part 2
class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refreshToken')
        id = decode_refresh_token(refresh_token)
        access_token = create_access_token(id)

        return Response({
            'token': access_token
        })


#user logout
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        #response.delete_cookie('jwt')   part 1
        response.delete_cookie(key="refreshToken")  #part 2
        response.data = {
            'message': 'success logout'
        }
        return response

