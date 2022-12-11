from dataclasses import fields
from tkinter import Widget
from django import forms
from django.forms import ModelForm
from .models import *

class CsvModelForm(ModelForm):
    class Meta :
        model = Csv
        fields = ('file_name',)

class addEmpform(ModelForm):
    class Meta: 
        model = emp

        fields = {
            'emp_id',
            'emp_name',
            'emp_shift',
        }
        labels = {
            'emp_id':'',
            'emp_name':'',
            'emp_shift':'',
        }

        Widgets ={
            'emp_id':forms.TextInput(attrs={'class':'inputFields','placeholder':'Enter Script Title Name *'}),
            'emp_name':forms.TextInput(attrs={'class':'form-input','placeholder':'Enter Emp Name'}),
            'emp_shift':forms.Select(attrs={'class':'cardSelect'}),
        }

class changeStatus(ModelForm):
    class Meta: 
        model = emp_status
        
        fields = {
            'status',
        }
        labels = {
            'emp':'',
            'status':'',
            'Date':'',
        }
        Widgets ={
            'emp':forms.Select(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'Date':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Emp Name'}),
        }