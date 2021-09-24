from fast_foods.models import Fastfood
from fast_foods.paginations import CustomPagination
from fast_foods.serializers import FastfoodSerializer
from rest_framework import viewsets

class FastFoodViewSetPagination(viewsets.ModelViewSet):
  queryset = Fastfood.objects.all()
  serializer_class = FastfoodSerializer
  pagination_class = CustomPagination

