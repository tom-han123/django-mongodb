from rest_framework import serializers
from .models import brand,bike_model,bike

class brandserializer(serializers.ModelSerializer):
    class Meta:
        model=brand
        fields=('brandId','brand_name')

class bike_modelserializer(serializers.ModelSerializer):
    class Meta:
        model=bike_model
        fields=('modelId','brandId','model_name')

class bikeserializer(serializers.ModelSerializer):
    class Meta:
        model=bike
        fields=('bikeId','modelId','bikename','bike_picture')
