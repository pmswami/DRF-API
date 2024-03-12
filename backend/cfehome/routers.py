from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet,ProductGenericViewSet

router = DefaultRouter()
# router.register('products-abc', ProductViewSet, basename='products')
router.register('products', ProductGenericViewSet, basename='products')
# print(router.urls)
urlpatterns = router.urls