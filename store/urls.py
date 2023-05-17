from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from . import views

"""
DefaultRouter: 
    - has api root page (http://127.0.0.1:8000/store/) 
    - returns json for any path like http://127.0.0.1:8000/store/products/1.json 
"""
router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)

# urlpatterns = router.urls
urlpatterns = [
    path("", include(router.urls))
    # some other pathes
]
