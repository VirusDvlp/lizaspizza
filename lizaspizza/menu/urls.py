from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('pizza/<int:pizza_id>', views.pizza, name='pizza')
]
