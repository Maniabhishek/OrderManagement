from django.contrib import admin
from .models import Associates ,Product, Order ,Tag

# Register your models here.
admin.site.register(Associates)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)