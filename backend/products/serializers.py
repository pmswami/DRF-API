from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer
from .models import Product
from .validators import validate_title, validate_title_no_hello, unique_product_title

class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail",
        lookup_field="pk",
        read_only=True
    )
    title=serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):

    # related_products = ProductInlineSerializer(source = "user.product_set.all", read_only=True, many=True)
    discount = serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail",
        lookup_field = "pk",
        read_only=True
    )
    edit_url = serializers.HyperlinkedIdentityField(
        view_name="product-edit",
        lookup_field = "pk",
        read_only=True
    )
    # email = serializers.EmailField(write_only=True)
    # title = serializers.CharField(validators=[validate_title])
    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])
    # name = serializers.CharField(source="title", read_only=True)
    # my_user_data = serializers.SerializerMethodField(read_only=True)
    owner = UserPublicSerializer(source="user", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Product
        fields = [
            'pk',
            "url",
            "edit_url",
            # "name",
            "owner",
            "title",
            'price',
            "sale_price",
            "discount",
            # "my_user_data"
            "email",
            "related_products"
        ]

    # def get_my_user_data(self, obj):
    #     return {
    #         "username": obj.user.username
    #     }
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

    # Validate Title
    # def validate_title(self, value):
    #     # qs = Product.objects.filter(title__exact=value)
    #     # qs = Product.objects.filter(title__iexact=value) # for case insensitive comparison
    #     request = self.context.get("request")
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value) # for case insensitive comparison
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value

    def get_discount(self, obj):
        try:
            if not hasattr(obj, "get_discount"):
                return None
            if not isinstance(obj, Product):
                return None
            return obj.get_discount()
        except:
            return None