from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, Customer, OrderItem, Order
from django.http import HttpResponse


def say_hello(request):
    # select_related (1)
    # prefetch_related (n)
    # query_set = Product.objects.prefetch_related("promotions").all()
    # query_set = Product.objects.select_related("collection").all()
    # query_set = Product.objects.prefetch_related("promotions").select_related("collection").all()

    # Get the last 5 orders with their customer and items includiing product
    query_set = (
        Order.objects.select_related("customer")
        .prefetch_related("orderitem_set__product")
        .order_by("-placed_at")[:5]
    )

    return render(request, "hello.html", {"name": "Ali", "products": list(query_set)})
