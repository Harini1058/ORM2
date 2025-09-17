from django.db import models
from django.contrib import admin
class exp2(models.Model):
    car_name= models.CharField()
    car_model = models.CharField()
    release_date = models.DateField()
    color = models.CharField()

class exp2Admin(admin.ModelAdmin):
    list_display = ('car_name', 'car_model', 'release_date', 'color')
# Create your models here.
