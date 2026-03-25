from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=255, label='Product name')
    description = forms.CharField(max_length=300, label='Product description')
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Product price')
    available = forms.BooleanField(initial=True, required=False, label='Available')
    image = forms.ImageField(required=False, label='Product image')

    def save(self):
        product = Product(
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],
            price=self.cleaned_data['price'],
            available=self.cleaned_data['available'],
            image=self.cleaned_data.get('image')
        )
        product.save()
        return product