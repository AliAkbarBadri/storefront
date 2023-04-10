from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Collection, Product
from .serializers import CollectionSerializer, ProductSerializer


@api_view(["GET", "POST"])
def products_list(request):
    if request.method == "GET":
        queryset = Product.objects.select_related("collection").all()
        serializer = ProductSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        # method1
        # if serializer.is_valid():
        #     serializer.validated_data
        #     return Response("ok")
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # method2: cleaner
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        return Response("ok")


@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view()
def collection_detail(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    serializer = CollectionSerializer(collection)
    return Response(serializer.data)
