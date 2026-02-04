from django.contrib import admin
from . models import Order

admin.site.register(Order);

class Admin(admin.ModelAdmin):
    list_display = ('orderID', 'userID', 'orderDate', 'itemName', 'orderQty', 'unitPrice', 'totalAmount', 'deliveryAddress')
