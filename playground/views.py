from django.shortcuts import render
from django.db.models import Value, F, Func, Count
from store.models import Product, Customer, OrderItem, Order


def say_hello(request):
    # customer's number of orders
    query_set = Customer.objects.annotate(
        order_number = Count('order')
    )
    _ = list(query_set)
    return render(request, "hello.html", {"name": "Ali"})
