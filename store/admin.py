from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.db.models import QuerySet
from django.utils.html import format_html, urlencode
from django.urls import reverse

from . import models


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "featured_product", "product_count"]
    list_per_page = 10
    list_select_related = ["featured_product"]
    search_fields = ["title"]

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


class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    min_num = 1
    autocomplete_fields = ["product"]
    extra = 0


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ["customer"]
    list_display = ["id", "placed_at", "customer"]
    list_per_page = 10
    inlines = [OrderItemInline]


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
    # customize form
    # only these fields in form of new product
    # fields = ["title", "unit_price"]
    # exclude these fields from form
    # exclude = ["description"]
    # readonly_fields = ["title"]
    prepopulated_fields = {"slug": ["title"]}

    autocomplete_fields = ["collection"]

    actions = ["clear_inventory"]
    list_display = ["title", "unit_price", "inventory_status", "collection_title"]
    list_editable = ["unit_price"]
    ordering = ["title"]
    list_per_page = 10
    list_select_related = ["collection"]
    list_filter = ["collection", "last_update", InventoryFilter]
    search_fields = ["title"]

    @admin.display(ordering="inventory")
    def inventory_status(self, product) -> str:
        if product.inventory < 10:
            return "LOW"
        return "OK"

    # @admin.display(ordering="collection") sort based on __str__
    def collection_title(self, product) -> str:
        return product.collection.title

    @admin.action(description="Clear inventory")
    def clear_inventory(self, request, queryset: QuerySet):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request, f"{updated_count} products were updated!", messages.WARNING
        )


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
