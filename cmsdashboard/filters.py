from cProfile import label
from cgitb import lookup
from dataclasses import field
from tkinter.tix import Select
import django_filters
from .models import emp,emp_status
from django_filters import CharFilter
from django import forms
from django.forms import ModelForm

class empfilter(django_filters.FilterSet):
    emp_name = CharFilter(field_name='emp_name', lookup_expr='icontains', label='')
    # emp_shift = Select(field_name='emp_shift', lookup_expr='icontains', label='')
    class Meta:
        model = emp
        fields ={'emp_name','emp_shift'}
        labels ={'emp_name':'','emp_shift':'',}


        exclude=['emp_id']


# class emp_statusfilter(django_filters.FilterSet):
#     class Meta:
#         model = emp_status
#         fields =['emp']