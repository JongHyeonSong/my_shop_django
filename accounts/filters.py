import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created",lookup_expr="gte")
    end_date = DateFilter(field_name="date_created",lookup_expr="lte")
    note =CharFilter(field_name='note', lookup_expr="icontains") # ignore 대소문자
    #위 커스텀note가 원래노트를덮어씀
    class Meta:
        model=Order
        fields='__all__'
        exclude=['customer','date_created']
        