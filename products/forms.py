from django import forms
from . import models

class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = ['title', 'category','brand','description','serie_number','cost_price','selling_price']