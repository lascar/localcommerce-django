from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='offers_index'),
    path('<int:id>', views.detail, name='offer_detail'),
    path('create', views.detail, name='offer_create'),
]
