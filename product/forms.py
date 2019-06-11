from django import forms
from . models import Product

class AddProductInfoForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['title','description','image','price','category']

    title =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Title','class': 'border w-100 p-2 bg-white text-capitalize'}))
    description=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Describe Your Product','class':'border p-3 w-100'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Price','class': 'border-0 py-2 w-100 price'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file d-none'}))
    # category = forms.ChoiceField(widget=forms.TextInput(attrs={'class': 'w-100'}))









        #         title =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username','class': 'border w-100 p-2 bg-white text-capitalize'}))
        # description=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Describe Your Product','class':'border p-3 w-100'}))
        # price = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Price','class': 'border-0 py-2 w-100 price'}))
        # # image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file d-none'}))
        # image = forms.ImageField()