from django.db import models
from core.models import Brand

# Create your models here.
class Car(models.Model):
    brand: models.ForeignKey(Brand,on_delete=models.RESTRICT)
    color = models.CharField(max_length=3, choices=[
        ('RED', 'red'),
        ('BLU', 'blue'),
        ('GRE', 'green'),
        ('BLK', 'black'),
    ], null=True,default=None)
    acceleration = models.IntegerField()
    create_timestamp = models.DateTimeField(auto_now_add=True)
