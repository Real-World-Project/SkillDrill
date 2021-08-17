from django.contrib import admin
from .models import Location, Services, Category, Order
# Register your models here.

admin.site.register(Location)
admin.site.register(Services)
admin.site.register(Category)
admin.site.register(Order)
