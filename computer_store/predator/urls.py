from django.shortcuts import render
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter(trailing_slash=False)
router.register(r"categories", views.Categories, basename="categories")
router.register(r"product-images", views.ProductImagesViewSet, basename="product-image")
urlpatterns = router.urls
# Create your views here.
urlpatterns += [
  path("products/<int:id>", views.ProductDetail.as_view(), name="product_detail"),
  path("products", views.Products.as_view(), name="products"),
]
