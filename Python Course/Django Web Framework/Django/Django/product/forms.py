from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        Model   = Product
        Fields  = [
            'Title',
            'Description',
            'Price'
        ] 