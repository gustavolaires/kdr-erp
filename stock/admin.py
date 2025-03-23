from django.contrib import admin

from .models import Manufacturer, Product, UnitType

admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(UnitType)
