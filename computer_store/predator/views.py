from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializer
from .models import Categories, Product
from .models import ProductImages as ProdImages


# Create your views here.
class Categories(viewsets.ModelViewSet):
    serializer_class = serializer.CategoriesSerializer
    queryset = Categories.objects.all()

class Products(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer_instance = serializer.ProductSerializer(products, many=True)
        return Response(serializer_instance.data, status=status.HTTP_200_OK)

    def post(self, request):
        print('here')
        data = request.data
        serializer_instance = serializer.ProductSerializer(data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Create product failed", "errors": serializer_instance.errors}, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get("id")
        if product_id is not None:
            try:
                product = Product.objects.get(id=product_id)
                serializer_class = serializer.ProductSerializer(product)
                images = ProdImages.objects.filter(productId=product_id)
                print(images)
                return Response(serializer_class.data, status=200)
            except Product.DoesNotExist:
                return Response({"message": "Product not found"}, status=400)

class ProductImagesViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.ProductImagesSerializer
    queryset = ProdImages.objects.all()
