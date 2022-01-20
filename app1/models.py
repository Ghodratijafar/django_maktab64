from django.db import models


# Create your models here.
class Car(models.Model):
    brand: models.CharField(max_length=30, null=False, default='Saipa')
    color = models.CharField(max_length=3, choices=[
        ('RED', 'red'),
        ('BLU', 'blue'),
        ('GRE', 'green'),
        ('BLK', 'black'),
    ], null=True,default=None)
    acceleration = models.IntegerField()
    create_timestamp = models.DateTimeField(auto_now_add=True)
