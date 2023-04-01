from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, Customer, OrderItem
from django.http import HttpResponse


def say_hello(request):
    """
    get objects with id and title.
    if you access to unit_price it will send a query for unit_price per object.
    """
    query_set = Product.objects.only("id", "title")
    
    """
    get objects with all feature except description.
    if you access to description it will send a query for description per object.
    """ 
    query_set = Product.objects.defer("description")

    return render(request, "hello.html", {"name": "Ali", "products": list(query_set)})
