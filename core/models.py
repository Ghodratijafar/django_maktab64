from django.db import models

# Create your models here.

class Brand(models.Model):
    country = models.CharField(max_length=20)
    name = models.CharField(max_length=20)