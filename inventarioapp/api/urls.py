
from rest_framework.routers import DefaultRouter

from inventarioapp.api.views import ProductViewSet

router = DefaultRouter()

router.register('products', ProductViewSet, 'product')

urlpatterns = router.urls