from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'about', 'max_presets', 'is_discount_preset', 'image', 'height_field', 'width_field', 'draft', 'file')
