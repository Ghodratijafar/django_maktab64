from django.db import models
from menu.models import *
from cashier.models import *


# Create your models here.
class Order(models.Model):
    number = models.IntegerField()
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE)
    status = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"{[self.number,self.table_id,self.status,self.timestamp]}"


class Order_items(models.Model):
    item_id = models.ForeignKey(Menuitem, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
