from decimal import Decimal
from pyexpat import model
from rest_framework import serializers
from store.models import Collection, Product


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "unit_price", "price_with_tax", "collection"]

    price_with_tax = serializers.SerializerMethodField(method_name="calc_tax")
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Product.objects.all(), view_name="collection-detail"
    # )

    def calc_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

    # this is just a example and is not real
    # def validate(self, data):
    #     if data["password"] != data["confirm_password"]:
    #         return serializers.ValidationError("Passwords do not match!")
    #     return data
