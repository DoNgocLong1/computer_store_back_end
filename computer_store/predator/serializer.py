from rest_framework import serializers

from . import models


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categories
        fields = ("id", "name", "image", "created_at", "updated_at")


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImages
        fields = ("image")


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    # dặt tên = method + biến bên trên sẽ tự động gán kết quả vào biến bên trên
    def get_images(self, obj):
        # Lấy tất cả các hình ảnh của sản phẩm có product_id tương ứng
        product_images = models.ProductImages.objects.filter(productId=obj.id)
        # Serialize các hình ảnh sử dụng ProductImagesSerializer
        serializer = ProductImagesSerializer(product_images, many=True)
        return serializer.data

    class Meta:
        model = models.Product
        fields = (
            "id",
            "name",
            "category",
            "brand",
            "price",
            "currency",
            "overview",
            "description",
            "sold",
            "inventory",
            "discount",
            "rate",
            "created_at",
            "updated_at",
            "images",
        )
