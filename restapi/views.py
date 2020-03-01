from django.shortcuts import render
from rest_framework import viewsets
from .serializer import LaptopSerializer,PhoneSerializer
from inventory.models import Laptop, Phone
# Create your views here.

class LaptopViewSet(viewsets.ModelViewSet):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer