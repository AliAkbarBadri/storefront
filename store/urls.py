from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductsList.as_view()),
    path("products/<int:pk>/", views.ProductDetail.as_view()),
    path("collections/", views.CollectionsList.as_view()),
    path("collections/<int:pk>/", views.CollectionsDetail.as_view()),
]
