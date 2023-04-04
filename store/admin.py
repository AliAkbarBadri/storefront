from django.contrib import admin
from django.db.models.aggregates import Count
from django.utils.html import format_html
from django.utils.html import urlencode
from django.urls import reverse
from django.db.models import QuerySet
from . import models


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "featured_product", "product_count"]
    list_per_page = 10
    list_select_related = ["featured_product"]

    @admin.display(ordering="products_count")
    def product_count(self, collection):
        url = (
            reverse("admin:store_product_changelist")
            + "?"
            + urlencode(
                {
                    "collection__id": str(collection.id),
                }
            )
        )

        return format_html("<a href={}>{}</a>", url, collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(products_count=Count("products"))


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "placed_at", "customer"]
    list_per_page = 10


class InventoryFilter(admin.SimpleListFilter):
    title = "inventory"
    parameter_name = "inventory"

    def lookups(self, request, model_admin):
        return [("<10", "Low")]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == "<10":
            return queryset.filter(inventory__lt=10)


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
    list_filter = ["collection", "last_update", InventoryFilter]

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
    list_display = ["first_name", "last_name", "membership", "order_count"]
    list_editable = ["membership"]
    ordering = ["first_name", "last_name"]
    search_fields = ["first_name__istartswith", "last_name__istartswith"]
    list_per_page = 10

    @admin.display(ordering="orders_count")
    def order_count(self, customer):
        url = (
            reverse("admin:store_order_changelist")
            + "?"
            + urlencode(
                {
                    "customer__id": str(customer.id),
                }
            )
        )

        return format_html("<a href={}>{}</a>", url, customer.orders_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(orders_count=Count("order"))
