from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=130)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    experience = models.IntegerField()
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    sector = models.CharField(max_length=50, choices=[('webdeveloper', 'WebDeveloper'),('backenddeveloper', 'BackendDeveloper'),('networking', 'Networking'),('ai/machinelearning', 'AI/MachineLearning'), ('cloudservices', 'CloudServices'),('admincustomersupport', 'AdminCustomerSupport')], default='AI/MachineLearning')
    skills = models.TextField()
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='programmer_pictures/', blank=True, null=True)

    def __str__(self) -> str:
        return self.name

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


class Client(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=130)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='client_pictures/', blank=True, null=True)

    def __str__(self) -> str:
        return self.name