from django.contrib import admin
from django.db.models.aggregates import Count
from . import models


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "featured_product", "product_count"]
    list_per_page = 10
    list_select_related = ["featured_product"]

    @admin.display(ordering="products_count")
    def product_count(self, collection):
        return collection.products_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(products_count=Count("products"))


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "placed_at", "customer"]
    list_per_page = 10


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    # if we want shoe __str__ of collection
    # list_display = ["title", "unit_price", "inventory_status", "collection"]

    # ow
    list_display = ["title", "unit_price", "inventory_status", "collection_title"]
    list_editable = ["unit_price"]
    ordering = ["title"]
    list_per_page = 10
    list_select_related = ["collection"]

    @admin.display(ordering="inventory")
    def inventory_status(self, product) -> str:
        if product.inventory < 10:
            return "LOW"
        return "OK"

    # @admin.display(ordering="collection") sort based on __str__
    def collection_title(self, product) -> str:
        return product.collection.title


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership"]
    list_editable = ["membership"]
    ordering = ["first_name", "last_name"]
    list_per_page = 10
