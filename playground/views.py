from django.shortcuts import render
from store.models import Product, Customer, OrderItem, Order, Collection
from tags.models import TaggedItem


def say_hello(request):
    # collection = Collection.objects.get(pk=11)
    # collection.featured_product = None
    # collection.save()

    # or
    collection = Collection.objects.filter(pk=12).update(featured_product_id=None)

    return render(request, "hello.html", {"name": "Ali"})
