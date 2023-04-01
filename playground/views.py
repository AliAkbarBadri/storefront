from django.shortcuts import render
from django.db.models import Value, F, Func, Count, ExpressionWrapper, DecimalField
from store.models import Product, Customer, OrderItem, Order


def say_hello(request):
    query_set = Product.objects.annotate(
        discounted_price=ExpressionWrapper(
            F("unit_price") * 0.8, output_field=DecimalField()
        )
    )
    _ = list(query_set)
    return render(request, "hello.html", {"name": "Ali"})
