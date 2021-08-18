from django.contrib import admin
from django.db import models


# Register your models here.
from .models import Customer

admin.site.register(Customer )