from rest_framework import serializers
from .models import CustomUser, ProgrammerProfile, ClientProfile
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_type', 'phone_number', 'address', 'bio', 'profile_picture']

class ProgrammerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammerProfile
        fields = ['experience', 'skills']

class ClientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = []

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'user_type', 'phone_number', 'address', 'bio', 'profile_picture']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            user_type=validated_data.get('user_type'),
            phone_number=validated_data.get('phone_number'),
            address=validated_data.get('address'),
            bio=validated_data.get('bio'),
            profile_picture=validated_data.get('profile_picture'),
        )
        if user.user_type == 'programmer':
            ProgrammerProfile.objects.create(user=user)
        elif user.user_type == 'client':
            ClientProfile.objects.create(user=user)
        return user
