from rest_framework import serializers

from . import models


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categories
        fields = ("id", "name", "image", "created_at", "updated_at")
