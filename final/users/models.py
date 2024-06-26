from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    first_name = None
    last_name = None
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
