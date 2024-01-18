from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class GetAllUserSerializer:
    class meta:
        model = User
        field = ("id", "email", "username", "password")
