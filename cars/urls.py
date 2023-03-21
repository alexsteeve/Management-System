from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='index'),
    path('create/', views.car_create, name='car_create'),
    path('update/<int:id>/', views.car_update, name='car_update'),
    path('delete/<int:id>/', views.car_delete, name='car_delete'),
    path('parts', views.part_list, name='parts'),
    path('parts/create/', views.part_create, name='part_create'),
    path('parts/update/<int:id>/', views.part_update, name='part_update'),
    path('parts/delete/<int:id>/', views.part_delete, name='part_delete'),
]