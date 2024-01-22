from django.shortcuts import render
from rest_framework import viewsets

from . import serializer
from .models import Categories


# Create your views here.
class Categories(viewsets.ModelViewSet):
    serializer_class = serializer.CategoriesSerializer
    queryset = Categories.objects.all()
