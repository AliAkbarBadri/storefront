from decimal import Decimal
from rest_framework import serializers
from store.models import Collection, Product


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(
        max_digits=6, decimal_places=2, source="unit_price"
    )
    price_with_tax = serializers.SerializerMethodField(method_name="calc_tax")
    collection = serializers.StringRelatedField()

    def calc_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
