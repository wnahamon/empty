from django import forms
from .models import Category

class ProductForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    title = forms.CharField(max_length=100)
    desc = forms.CharField(max_length=400)
    price = forms.DecimalField(max_digits=10, decimal_places=0)