from django.shortcuts import render
from django.db import connection
from store.models import Product, Customer, OrderItem, Order, Collection


# decorate all say_hello function to run as a transaction
@transaction.atomic()
def say_hello(request):
    # run raw query that the result fits in model
    query_set = Product.objects.raw("select * from store_product")
    query_set = Product.objects.raw("select ifd, title from store_product")
    
    # otherwise
    with connection.cursor() as cursor:
        cursor.execute("select * from store_product")
        # run stored_procedure, the cleaner way
        cursor.callproc("get_products", [1,2])
        row = cursor.fetchone()
    return render(request, "hello.html", {"name": "Ali"})
