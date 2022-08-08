from ast import mod
from django.db import models

# Create your models here.

class brand(models.Model):
    brandId=models.AutoField(primary_key=True)
    brand_name=models.CharField(max_length=30)

    def __str__(self):
        return self.brand_name

class bike_model(models.Model):
    modelId=models.AutoField(primary_key=True)
    brandId=models.ForeignKey(brand,on_delete=models.CASCADE)
    model_name=models.CharField(max_length=30)

    def __str__(self):
        return self.model_name

class bike(models.Model):
    bikeId=models.AutoField(primary_key=True)
    modelId=models.ForeignKey(bike_model,on_delete=models.CASCADE)
    bikename=models.CharField(max_length=30)
    bike_picture=models.ImageField(null=True)
    
