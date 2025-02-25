from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    bar_code = models.CharField(max_length=64)
    amount = models.IntegerField()
    manufacturer_reference = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.bar_code} - {self.name}'


