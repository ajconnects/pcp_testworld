from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializer import *

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
            categories=category,
            sector=data['sector'],
            skills=data['skills'],
            bio=data['bio'],
            profile_picture=data.get('profile_picture', None)
        )

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
        elif category_name == 'admin/customersupport':
            AdminCustomerSupport.objects.create(programmer=programmer)

        return Response(ProgrammerSerializer(programmer).data, status=status.HTTP_201_CREATED)

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
