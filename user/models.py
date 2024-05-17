from django.contrib.auth.models import AbstractUser
from django.db import models


class Admin(AbstractUser):
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Customer(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40, null=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)

