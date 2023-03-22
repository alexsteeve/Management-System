from django.urls import path
from . import views
from .views import CarDetailView

urlpatterns = [
    path('', views.car_list, name='index'),
    path('create/', views.car_create, name='car_create'),
    path('update/<int:id>/', views.car_update, name='car_update'),
    path('delete/<int:id>/', views.car_delete, name='car_delete'),
    path('parts', views.part_list, name='parts'),
    path('parts/create/', views.part_create, name='part_create'),
    path('parts/update/<int:id>/', views.part_update, name='part_update'),
    path('parts/delete/<int:id>/', views.part_delete, name='part_delete'),
    path('<int:VIN>/', views.CarDetailView.as_view(), name='car_detail'),
    # path('<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
]