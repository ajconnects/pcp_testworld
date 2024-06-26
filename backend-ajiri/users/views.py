from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CustomUser, ProgrammerProfile, ClientProfile
from .serializers import UserSerializer, RegisterSerializer, ProgrammerProfileSerializer, ClientProfileSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class ProgrammerProfileView(generics.RetrieveUpdateAPIView):
    queryset = ProgrammerProfile.objects.all()
    serializer_class = ProgrammerProfileSerializer

    def get_object(self):
        return self.request.user.programmerprofile

class ClientProfileView(generics.RetrieveUpdateAPIView):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer

    def get_object(self):
        return self.request.user.clientprofile
