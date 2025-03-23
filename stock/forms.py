from django import forms
from stock.models import Product

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        fields = ["name", "bar_code", "manufacturer", "manufacturer_code", "unit_type", "amount", "unit_price"]