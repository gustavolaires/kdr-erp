from django import forms
from stock.models import Product

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.__class__.__name__ in ['ModelChoiceField']:
                visible.field.widget.attrs['class'] = 'form-select'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        fields = ["name", "bar_code", "manufacturer", "manufacturer_code", "unit_type", "amount", "unit_price"]
        labels = {
            "bar_code": "Código de barras",
            "name": "Nome",
            "manufacturer": "Fabricante",
            "manufacturer_code": "Código do fabricante",
            "unit_type": "Tipo de unidade",
            "amount": "Quantidade",
            "unit_price": "Preço unitário",
        }