from rest_framework import serializers
from inventory.models import Laptop, Phone

class LaptopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Laptop
        fields = ['id', 'name', 'price', 'status']

class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phone
        fields = ['id', 'name', 'price', 'status']