from django.contrib import admin
from .models import RealProduct

@admin.register(RealProduct)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product', 'variety', 'aspect', 'packaging', 'size',
            'caliber']
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 50
    fields = ['name', 'product', 'variety', 'aspect', 'packaging', 'size',
            'caliber']
