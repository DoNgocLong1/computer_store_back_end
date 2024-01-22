from django.shortcuts import render
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter(trailing_slash=False)
router.register(r"categories", views.Categories, basename="categories")
urlpatterns = router.urls
# Create your views here.
# urlpatterns = [path("categories", views.Categories.as_view(), name="Categories")]