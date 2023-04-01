from django.shortcuts import render
from django.db.models import Value, F
from store.models import Product, Customer, OrderItem, Order


def say_hello(request):
    query_set = Customer.objects.annotate(is_new=Value(True))
    query_set = Customer.objects.annotate(new_id=F("id") + 1)
    _ = list(query_set)
    return render(request, "hello.html", {"name": "Ali"})
