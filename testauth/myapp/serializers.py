from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        RefreshToken(self.token).blacklist()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims if needed
        return token

    def validate(self, attrs):
        # Here we use email instead of username
        credentials = {
            'email': attrs.get('email'),
            'password': attrs.get('password')
        }

        user = CustomUser.objects.filter(email=credentials['email']).first()
        if user and user.check_password(credentials['password']):
            token = super().get_token(user)
            return {
                'refresh': str(token),
                'access': str(token.access_token),
            }
        else:
            raise serializers.ValidationError('Invalid email or password')

