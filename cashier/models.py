from django.db import models
from catagory.models import *
# Create your models here.



class Table(models.Model):
    table_number = models.IntegerField()
    cafe_position = models.CharField(max_length=30)
    capacity = models.IntegerField()
    status = models.CharField(max_length=20)

    # def __str__(self):
    #     return f"table_number:{self.table_number}\ncafe_position:{self.cafe_position}\ncapacity:{self.capacity}\nstatus:{self.status}"


