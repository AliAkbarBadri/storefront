from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, Customer, OrderItem
from django.http import HttpResponse


def say_hello(request):
    # values
    # dictionary
    # query_set = Product.objects.values('id', 'title', 'collection__title')

    # tuple
    # query_set = Product.objects.values_list('id', 'title', 'collection__title')

    # select products that have been ordered and sort them by title
    query_set = (
        OrderItem.objects.values(title=F("product__title")).distinct().order_by("title")
    )
    return render(request, "hello.html", {"name": "Ali", "products": list(query_set)})
