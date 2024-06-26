from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    first_name = None
    last_name = None
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Programmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='programmer')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    experience = models.IntegerField()
    rate = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(10), MaxValueValidator(100)])
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='programmers')
    skills = models.TextField()
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='programmer_pictures/', blank=True, null=True)
    cv = models.ImageField(upload_to='programmer_cv/', blank=True, null=True)

    def __str__(self):
        return self.user.email if self.user else 'No User'

class FrontEndDeveloper(models.Model):
    programmer = models.OneToOneField(Programmer, on_delete=models.CASCADE)

class BackEndDeveloper(models.Model):
    programmer = models.OneToOneField(Programmer, on_delete=models.CASCADE)

class DevOps(models.Model):
    programmer = models.OneToOneField(Programmer, on_delete=models.CASCADE)

class DS_ML(models.Model):
    programmer = models.OneToOneField(Programmer, on_delete=models.CASCADE)

class CloudServices(models.Model):
    programmer = models.OneToOneField(Programmer, on_delete=models.CASCADE)

class SysAdmin(models.Model):
    programmer = models.OneToOneField(Programmer, on_delete=models.CASCADE)

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='client_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.email if self.user else 'No User'
