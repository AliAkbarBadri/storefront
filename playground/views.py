from django.shortcuts import render
from django.db import connection
from store.models import Product, Customer, OrderItem, Order, Collection


def say_hello(request):
    return render(request, "hello.html", {"name": "Ali"})
