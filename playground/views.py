from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, Customer
from django.http import HttpResponse


def say_hello(request):
    # product = Product.objects.get(pk=1)
    # product = Product.objects.filter(pk=1).first()
    # print(product.title)

    # keyword = value
    # query_set = Product.objects.filter(unit_price=20)
    # query_set = Product.objects.filter(unit_price__gt=20)
    # query_set = Product.objects.filter(unit_price__range=(20, 30))
    # query_set = Product.objects.filter(collection__id__range=(1,3))
    # query_set = Product.objects.filter(title__icontains='coffee')
    # query_set = Product.objects.filter(last_update__year=2021)
    # query_set = Product.objects.filter(description__isnull=True)

    # query_set = Customer.objects.filter(email__icontains=".com")
    # Order items for products in collection 3
    # query_set = Order.objects.filter(product__collection_id=3)
    # return render(request, "hello.html", {"name": "Ali", "products": list(query_set)})
    
    # and 
    # query_set = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    # query_set = Product.objects.filter(Q(inventory__lt=10) & Q(unit_price__lt=20))
    
    # or. not
    # query_set = Product.objects.filter(Q(inventory__lt=10) or ~Q(unit_price__lt=20))
    
    # Products: inventory=price
    # query_set = Product.objects.filter(inventory= F("unit_price"))
    # query_set = Product.objects.filter(inventory= F("collection__id"))
    return render(request, "hello.html", {"name": "Ali", "products": list(query_set)})
