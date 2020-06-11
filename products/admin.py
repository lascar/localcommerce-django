from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['valid', 'name', 'variety',]
    list_filter = ['name', 'variety',]
    search_fields = ['name']
    list_per_page = 50
    fields = ['valid', 'name', 'variety',]
