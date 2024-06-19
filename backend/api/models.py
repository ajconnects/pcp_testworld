from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.email

class Programmer(User):
    experience = models.IntegerField()
    rate = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(10), MaxValueValidator(100)])
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    skills = models.TextField()
    cv = models.ImageField(upload_to='programmer_cv/', blank=True, null=True)

class Client(User):
    pass

class WebDeveloper(models.Model):
    programmer = models.OneToOneField(Programmer, on_delete=models.CASCADE)

class BackEndDeveloper(models.Model):
    programmer = models.OneToOneField(Programmer, on_delete=models.CASCADE)

class Networking(models.Model):
    programmer = models.OneToOneField(Programmer, on_delete=models.CASCADE)

class MachineLearning(models.Model):
    programmer = models.OneToOneField(Programmer, on_delete=models.CASCADE)

class CloudServices(models.Model):
    programmer = models.OneToOneField(Programmer, on_delete=models.CASCADE)

class AdminCustomerSupport(models.Model):
    programmer = models.OneToOneField(Programmer, on_delete=models.CASCADE)