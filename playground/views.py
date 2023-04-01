from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, Customer
from django.http import HttpResponse


def say_hello(request):
    # limit
    query_set = Product.objects.all()[5:10]
    return render(request, "hello.html", {"name": "Ali", "products": list(query_set)})
