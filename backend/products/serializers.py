from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', "title", 'price', "sale_price", "discount"]

    def get_discount(self, obj):
        return obj.get_discount()