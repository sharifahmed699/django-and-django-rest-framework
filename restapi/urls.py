from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('laptops', views.LaptopViewSet)
router.register('phones', views.PhoneViewSet)



urlpatterns = [
    path('', include(router.urls))
   
]
