from django.urls import path
from django.urls.conf import include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)

# urlpatterns = router.urls
urlpatterns = [
    path("", include(router.urls))
    # some other pathes
]
