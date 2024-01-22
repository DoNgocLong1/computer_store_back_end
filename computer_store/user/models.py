import django.utils.timezone
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    avatar = models.ImageField(
        upload_to="user/avatar/", null=True, blank=True, default=None
    )
    full_name = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
