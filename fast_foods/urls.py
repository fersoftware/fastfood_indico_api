from django.urls import include, path
from rest_framework.routers import DefaultRouter
from fast_foods.views import FastFoodViewSetPagination

app_name = 'fast_foods'

router = DefaultRouter(trailing_slash=False)
router.register(r'foods', FastFoodViewSetPagination)

urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]
