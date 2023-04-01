from django.shortcuts import render
from django.db.models.aggregates import Count, Min
from store.models import Product, Customer, OrderItem, Order
from django.http import HttpResponse


def say_hello(request):
    result = Product.objects.filter(id__lte=500).aggregate(
        count_id=Count("id"), min_price=Min("unit_price")
    )

    return render(request, "hello.html", {"name": "Ali", "result": result})
 