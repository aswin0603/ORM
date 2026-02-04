# Ex02 Django ORM Web Application
## Date: 04-02-2026

## AIM
To develop a Django application to manage an online food delivery platform like Zomato/Swiggy using Object Relational Mapping (ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
### admin.py
```python
from django.contrib import admin
from . models import Order

admin.site.register(Order);

class Admin(admin.ModelAdmin):
    list_display = ('orderID', 'userID', 'orderDate', 'itemName', 'orderQty', 'unitPrice', 'totalAmount', 'deliveryAddress')

```

### models.py
```python
from django.db import models
from django.contrib import admin

class Order(models.Model):
    orderID = models.IntegerField(primary_key=True)
    userID = models.IntegerField()
    orderDate = models.DateField()
    itemName = models.CharField(max_length=20)
    orderQty = models.IntegerField()
    unitPrice = models.IntegerField()
    totalAmount = models.IntegerField()
    deliveryAddress = models.CharField()
```


## OUTPUT

<img width="1914" height="836" alt="image" src="https://github.com/user-attachments/assets/bdf5ea84-04fa-4d9a-9eff-7470fbf4c573" />



## RESULT
Thus the program for creating a database using ORM hass been executed successfully

</hr>

### NAME : ASWIN B
### REGISTER NUMBER : 212224110007
