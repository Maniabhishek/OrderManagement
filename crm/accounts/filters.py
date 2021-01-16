from django.db.models import fields
import django_filters
from .models import *
from django_filters import CharFilter, DateFilter

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created",lookup_expr="gte")
    end_date = DateFilter(field_name="date_created",lookup_expr="lte")
    note = CharFilter(field_name ="note",lookup_expr="icontains")

    # name = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer','date_created']
