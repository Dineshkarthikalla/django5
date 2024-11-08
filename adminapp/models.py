from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title






from django.db import models
from django.contrib.auth.models import User

class StudentList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    Register_Number = models.CharField(max_length=20, unique=True)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Register_Number

from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    description = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name} - {self.email}'