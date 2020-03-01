
from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name="index"),
    path('laptop/', views.laptop, name="Laptop"),
    path('phone/', views.phone, name="Phone"),
    path('insert_laptop/', views.insert_laptop, name="Insert_laptop"),
    path('insert_phone/', views.insert_phone, name="Insert_phone"),
    path('update_laptop/<int:pk>', views.update_laptop, name="update_laptop"),
    path('update_phone/<int:pk>', views.update_phone, name="update_phone"),
    path('laptop_delete/<int:pk>', views.laptop_delete, name="laptop_delete"),
    path('phone_delete/<int:pk>', views.phone_delete, name="phone_delete"),


]
