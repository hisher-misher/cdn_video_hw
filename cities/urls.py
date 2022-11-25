from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.city_list, name='city_list'),
    path('view/<int:pk>', views.city_view, name='city_view'),
    path('new', views.city_create, name='city_new'),
    path('edit/<int:pk>', views.city_update, name='city_edit'),
    path('delete/<int:pk>', views.city_delete, name='city_delete'),
    path('clothest/', views.clothest_cities, name='clothest_cities'),
]