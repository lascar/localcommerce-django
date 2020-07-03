from django.contrib import admin
from .models import ConcreteProduct

@admin.register(ConcreteProduct)
class ProductAdmin(admin.ModelAdmin):
    pass
