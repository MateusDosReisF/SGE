from django import forms
from django.core.exceptions import ValidationError
from . import models

class OutflowForm(forms.ModelForm):

    class Meta:
        model = models.Outflow
        fields = ['product', 'quantity','description']

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')
        if quantity > product.quantity:
            raise ValidationError(f'A quantidade Disponível em estoque para o produto {product.title} é de {product.quantity} unidades.')
        return quantity