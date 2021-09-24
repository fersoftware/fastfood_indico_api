from rest_framework import serializers
from fast_foods.models import Fastfood


class FastfoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fastfood
        fields = (
                'id',
                'address',
                'categories',
                'city',
                'country',
                'name',
                'postalCode',
                'province',
                'websites',
                'latitude',
                'longitude',)