# Ex02 Django ORM Web Application
## Date: 17.09.2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 5 Car 

## PROGRAM

```
models.py
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
admin.py
from django.contrib import admin
from.models import exp2,exp2Admin
admin.site.register(exp2,exp2Admin)
```

## OUTPUT
![alt text](<Screenshot 2025-09-17 133945.png>)



## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
