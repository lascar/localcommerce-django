from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['active', 'name', 'varieties', 'aspects', 'packagings',
            'sizes', 'calibers']
    list_filter = ['active', 'name']
    search_fields = ['name']
    list_per_page = 50
    fields = ['active', 'name', 'varieties', 'aspects','packagings', 'sizes',
            'calibers']
