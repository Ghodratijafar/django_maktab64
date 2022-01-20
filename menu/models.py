from django.db import models
from catagory.models import *
from cashier.models import *
# Create your models here.
class Menuitem(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.CharField(max_length=50)
    discount = models.IntegerField(default=0)
    catagory = models.ForeignKey(Catagory, models.CASCADE)


class Receipts(models.Model):
    table_id = models.ForeignKey(Table,on_delete=models.CASCADE)
    total_price = models.IntegerField(default=0)
    final_price = models.IntegerField(default=0)
    time_stamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30)