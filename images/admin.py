from django.contrib import admin
from .models import Images, Category, Location

# Register your models here.
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Images)