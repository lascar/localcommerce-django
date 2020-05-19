from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'active', 'varieties',
                    'aspects', 'packagings', 'sizes', 'calibers']
    list_filter = ['active', 'category']
    search_fields = ['name']
    list_per_page = 50
    fields = ['active', 'name', 'category', 'varieties',
              'aspects', 'packagings', 'sizes', 'calibers']
