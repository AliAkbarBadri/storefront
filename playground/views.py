from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Customer, OrderItem, Order
from tags.models import TaggedItem


def say_hello(request):
    # tags of a product id
    content_type = ContentType.objects.get_for_model(Product)
    query_set = TaggedItem.objects.select_related("tag").filter(
        content_type=content_type,  # id of store product in django_content_type table
        object_id=1,  # target product_id
    )
    return render(request, "hello.html", {"name": "Ali", "tags": list(query_set)})
