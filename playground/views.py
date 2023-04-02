from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Customer, OrderItem, Order
from tags.models import TaggedItem


def say_hello(request):
    # tags of a product id
    query_set = TaggedItem.objects.get_tags_for(Product, 1)
    return render(request, "hello.html", {"name": "Ali", "tags": list(query_set)})
