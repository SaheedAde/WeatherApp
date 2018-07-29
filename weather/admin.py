from django.contrib import admin

#register the model
from .models import City

# Register your models here.
admin.site.register(City)