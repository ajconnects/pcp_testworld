from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password
from django.templatetags.static import static
from django.conf import settings

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ProgrammerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    profile_picture = serializers.ImageField(max_length=None, use_url=True, required=False)
    categories = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='categories', write_only=True
    )

    class Meta:
        model = Programmer
        fields = ['user', 'phone_number', 'address', 'experience', 'rate', 'categories', 'category_id', 'skills', 'bio', 'profile_picture', 'cv']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['password'] = make_password(user_data['password'])  # Hash the password before saving
        user = User.objects.create(**user_data)
        programmer = Programmer.objects.create(user=user, **validated_data)
        return programmer

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user = instance.user
            user.name = user_data.get('name', user.name)
            user.email = user_data.get('email', user.email)
            if 'password' in user_data:
                user.set_password(user_data['password'])  # Update the password correctly
            user.save()

        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.address = validated_data.get('address', instance.address)
        instance.experience = validated_data.get('experience', instance.experience)
        instance.rate = validated_data.get('rate', instance.rate)
        instance.skills = validated_data.get('skills', instance.skills)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.cv = validated_data.get('cv', instance.cv)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.save()

        return instance

class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    profile_picture = serializers.ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = Client
        fields = ['user', 'phone_number', 'address', 'bio', 'profile_picture']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['password'] = make_password(user_data['password'])  # Hash the password before saving
        user = User.objects.create(**user_data)
        client = Client.objects.create(user=user, **validated_data)
        return client

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.address = validated_data.get('address', instance.address)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.save()

        user.name = user_data.get('name', user.name)
        user.email = user_data.get('email', user.email)
        if 'password' in user_data:
            user.password = make_password(user_data['password'])  # Hash the password before saving
        user.save()

        return instance

class PublicProgrammerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')
    categories = serializers.CharField(source='categories.name')
    profile_picture = serializers.SerializerMethodField()

    class Meta:
        model = Programmer
        fields = ['id', 'name', 'skills', 'categories', 'profile_picture']

    def get_profile_picture(self, obj):
        #print(f"Object in get_profile_picture: {type(obj)}")  # Debugging line
        if obj.profile_picture.name:
            #print(f"Profile picture URL: {settings.MEDIA_URL}{obj.profile_picture.name}")  # Debugging line
            return f"http://127.0.0.1:8000/{settings.MEDIA_URL}{obj.profile_picture.name}"
        return static('programmer_pictures/default_image.jpg')

class FrontEndDeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontEndDeveloper
        fields = '__all__'

class BackEndDeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackEndDeveloper
        fields = '__all__'

class DevOpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevOps
        fields = '__all__'

class Ds_MlSerializer(serializers.ModelSerializer):
    class Meta:
        model = DS_ML
        fields = '__all__'

class CloudServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudServices
        fields = '__all__'

class SysAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysAdmin
        fields = '__all__'
