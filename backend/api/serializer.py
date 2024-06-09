from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProgrammerSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(max_length=None, use_url=True, required=False)
    categories = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='categories', write_only=True
    )

    class Meta:
        model = Programmer
        fields = '__all__'

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

class ClientSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = Client
        fields = '__all__'