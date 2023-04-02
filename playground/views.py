from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Customer, OrderItem, Order, Collection
from tags.models import TaggedItem


def say_hello(request):
    # collection = Collection()
    # collection.title = "Video Game"
    # collection.featured_product = Product(pk=1)
    # or: collection.featured_product_id = 1
    # collection.save()

    # or
    # collection = Collection(title="Video Game", featured_product_id=1)
    # collection.save()

    # or
    collection = Collection.objects.create(title="Folan", featured_product_id=11)

    return render(request, "hello.html", {"name": "Ali"})
