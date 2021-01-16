from django.db.models import fields
from django.db import django_filters
from .models import *

class OrderFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Order
        fields = '__all__'
