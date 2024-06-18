from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'phone_number', 'address', 'bio', 'profile_picture')

class ProgrammerSerializer(UserSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Programmer
        fields = UserSerializer.Meta.fields + ('password', 'experience', 'rate', 'categories', 'skills', 'cv')

    def create(self, validated_data):
        password = validated_data.pop('password')
        programmer = Programmer(**validated_data)
        programmer.set_password(password)
        programmer.save()
        return programmer

class ClientSerializer(UserSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Client
        fields = UserSerializer.Meta.fields + ('password',)

    def create(self, validated_data):
        password = validated_data.pop('password')
        client = Client(**validated_data)
        client.set_password(password)
        client.save()
        return client

class WebDeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebDeveloper
        fields = '__all__'

class BackEndDeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackEndDeveloper
        fields = '__all__'

class NetworkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Networking
        fields = '__all__'

class MachineLearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineLearning
        fields = '__all__'

class CloudServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudServices
        fields = '__all__'

class AdminCustomerSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminCustomerSupport
        fields = '__all__'

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD

    def validate(self, attrs):
        # Update attrs to replace 'email' with 'username'
        attrs[self.username_field] = attrs.pop('email', None)
        return super().validate(attrs)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['name'] = user.name
        token['email'] = user.email
        return token