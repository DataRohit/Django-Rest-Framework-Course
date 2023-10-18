# Import django admin
from django.contrib import admin

# Import all models
from .models import *

# Register your models here.
admin.site.register(Product)
