from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import viewsets
from rest_framework.response import Response

from fast_foods.models import Fastfood
from fast_foods.serializers import FastfoodSerializer
from home.forms import FastfoodForm

class FastFoodViewSet(viewsets.ModelViewSet):
  queryset = Fastfood.objects.all()
  serializer_class = FastfoodSerializer

  def create(self, request, *args, **kwargs):
    serializer = FastfoodSerializerCreate(data=request.data)
    serializer.is_valid(raise_exception=True)
    lastid = Fastfood.objects.latest('id')
    serializer.save(pk=lastid.id+1)
    return Response(serializer.data)


class FastFoodListView(ListView):
    model = Fastfood
    def get_queryset(self, *args, **kwargs):
        queryset = Fastfood.objects.all().order_by('-id')
        return queryset


class FastFoodCreateView(CreateView):
    model = Fastfood
    form_class = FastfoodForm
    success_url = "/fastfood/"


class FastFoodUpdateView(UpdateView):
    model = Fastfood
    form_class = FastfoodForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('fastfood_listView')


class FastFoodDeleteView(DeleteView):
    model = Fastfood

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('fastfood_listView')