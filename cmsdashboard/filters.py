from cProfile import label
from cgitb import lookup
from dataclasses import field
import django_filters
from .models import emp,
from django_filters import CharFilter


class empfilter(django_filters.FilterSet):
    emp_name = CharFilter(field_name='emp_name', lookup_expr='icontains', label='')
    class Meta:
        model = emp
        fields ={'emp_name','emp_shift'}
        labels ={'emp_name':'','emp_shift':'',}


        exclude=['emp_id']

