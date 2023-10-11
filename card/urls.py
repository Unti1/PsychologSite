from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('record', views.record, name='record'),
    path('add/', views.add_order, name='add_order'),
]
