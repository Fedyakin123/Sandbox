from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    gender = models.CharField(max_length=2, null = True, blank = True)
    country = models.CharField(max_length=50, null = True, blank = True)

