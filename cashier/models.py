from django.db import models
from catagory.models import *
# Create your models here.



class Table(models.Model):
    table_number = models.IntegerField()
    cafe_positio = models.CharField(max_length=30)
    capacity = models.IntegerField()
    status = models.CharField(max_length=20)


