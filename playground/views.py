from django.shortcuts import render
from store.models import Product, Customer, OrderItem, Order, Collection
from tags.models import TaggedItem


def say_hello(request):
    # delete single object
    collection = Collection(pk=11)
    collection.delete()

    # delete single or multiple objects
    # collection = Collection.objects.filter(id__gt=10).delete()

    return render(request, "hello.html", {"name": "Ali"})
