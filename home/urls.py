from django.urls import path
from .views import FastFoodListView, FastFoodCreateView, FastFoodUpdateView,FastFoodDeleteView

urlpatterns = [
    path('', FastFoodListView.as_view(), name='fastfood_listView'),
    path('create/', FastFoodCreateView.as_view(), name='fastfood_CreateView'),
    path('update/<int:pk>/', FastFoodUpdateView.as_view(), name='fastfood_UpdateView'),
    path('delete/<int:pk>', FastFoodDeleteView.as_view(), name='delete_view'),
]