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
    create_at = models.DateField(default=django.utils.timezone.now, editable=False)
    update_at = models.DateField(default=django.utils.timezone.now, editable=False)
