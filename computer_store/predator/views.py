from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializer
from .models import Categories, Product, ProductImages


# Create your views here.
class Categories(viewsets.ModelViewSet):
    serializer_class = serializer.CategoriesSerializer
    queryset = Categories.objects.all()


class ProductDetail(APIView):
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get("id")
        if product_id is not None:
            product = Product.objects.get(id=product_id)
            serializer_class = serializer.ProductSerializer(product, many=False)
            images = ProductImages.objects.filter(productId=product_id)
            print(images)
            return Response(serializer_class.data, status=200)

        else:
            return Response({message: "Product not found"}, status=400)
