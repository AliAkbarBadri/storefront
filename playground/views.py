from django.shortcuts import render
from store.models import Product
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
    query_set = Product.objects.filter(last_update__year=2021)
    # query_set = Product.objects.filter(description__isnull=True)
    return render(request, "hello.html", {"name": "Ali", "products": list(query_set)})
