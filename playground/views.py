from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, Customer
from django.http import HttpResponse


def say_hello(request):
    # unit_prce ASC order, title DESC
    query_set = Product.objects.order_by('unit_price', '-title')
    
    # first, last
    product = Product.objects.earliest('unit_price')
    product = Product.objects.last('unit_price')
    return render(request, "hello.html", {"name": "Ali", "products": list(query_set)})
