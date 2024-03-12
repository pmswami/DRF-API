from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    # url = serializers.HyperlinkedIdentityField(
    #     view_name="product-detail",
    #     lookup_field = "pk"
    # )
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = ['pk', "title", 'price', "sale_price", "discount", "email"]

    # def get_url(self, obj):
    #     # return f"/api/products/{obj.pk}/"
    #     # return f"/api/products/{obj.id}/"
    #     request = self.context.get("request")
    #     # print(request)
    #     # return request
    #     if request is None:
    #         return None
    #     # return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)
    #     return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    # def create(self, validated_data):
    #     # email = validated_data.pop("email")
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     instance.title=validated_data.get("title")
    #     return instance

    def get_discount(self, obj):
        try:
            if not hasattr(obj, "get_discount"):
                return None
            if not isinstance(obj, Product):
                return None
            return obj.get_discount()
        except:
            return None