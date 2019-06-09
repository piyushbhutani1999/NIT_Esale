from django import forms
from . models import Product

class AddProductInfoForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['title','description','image']
        widgets={
            'price':forms.NumberInput(),
        }