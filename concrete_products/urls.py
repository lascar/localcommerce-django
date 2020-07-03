from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='concrete_products_index'),
    path('<int:id>', views.detail, name='concrete_product_detail'),
    path('create', views.detail, name='concrete_product_create'),
]
