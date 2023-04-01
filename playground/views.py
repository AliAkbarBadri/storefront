from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, Customer
from django.http import HttpResponse


def say_hello(request):
    query_set = []
    return render(request, "hello.html", {"name": "Ali", "products": list(query_set)})
