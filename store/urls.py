from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views  

"""
DefaultRouter: 
    - has api root page (http://127.0.0.1:8000/store/) 
    - returns json for any path like http://127.0.0.1:8000/store/products/1.json 
"""
router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)

products_router = routers.NestedDefaultRouter(router, "products", lookup="product")
products_router.register("reviews", views.ReviewViewSet, "product-reviews")


# urlpatterns = router.urls + products_router.urls
urlpatterns = [
    path("", include(router.urls)),
    path("", include(products_router.urls))
    # some other pathes
]
