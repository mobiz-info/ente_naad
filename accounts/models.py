from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('Admin', 'Admin'),
        ('Panchayath', 'Panchayath'),
        ('Muncipality', 'Muncipality'),
        ('Corporation', 'Customer'),
        
    )
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, null=True, blank=True)
