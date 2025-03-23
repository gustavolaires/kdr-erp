from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}'

class UnitType(models.Model):
    name = models.CharField(max_length=128)
    symbol = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.symbol}'

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True)
    bar_code = models.CharField(max_length=64, null=True)
    amount = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    unit_type = models.ForeignKey(UnitType, on_delete=models.SET_NULL, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    manufacturer_code = models.CharField(max_length=64, null=True)

    def __str__(self):
        return f'{self.bar_code} - {self.name}'


