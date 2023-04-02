from django.shortcuts import render
from django.db import transaction
from store.models import Product, Customer, OrderItem, Order, Collection


# decorate all say_hello function to run as a transaction
@transaction.atomic()
def say_hello(request):
    order = Order.objects.create(customer_id=1)
    item = OrderItem.objects.create(
        order=order, product_id=1, quantity=1, unit_price=10
    )
    return render(request, "hello.html", {"name": "Ali"})

# when we want run atomic part of function
# def say_hello(request):
#     # ....
#     with transaction.atomic():
#         order = Order.objects.create(customer_id=1)
#         item = OrderItem.objects.create(
#             order=order, product_id=1, quantity=1, unit_price=10
#         )
    return render(request, "hello.html", {"name": "Ali"})
