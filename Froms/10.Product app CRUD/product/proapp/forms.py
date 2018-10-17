from django import forms
from proapp.models import Product 
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

        productId=forms.IntegerField(
            widget=forms.TextInput(attrs={
                'class':'form-control',
                "placeholder":"Enter Product Id",
            })
        )
        productName=forms.CharField(
            widget=forms.TextInput(attrs={
                'class':'form-control',
                "placeholder":"Enter Product Name",
            })
        )
        productCost=forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Product Cost',
            })
        )
        productQuantity=forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Product Quantity',
            })
        )
        productDescription=forms.CharField(
            widget=forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Product Description',
            })
        )