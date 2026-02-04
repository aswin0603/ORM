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