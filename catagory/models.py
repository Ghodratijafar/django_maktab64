from django.db import models

# Create your models here.
class Catagory(models.Model):
    title = models.CharField(max_length=30)
    root = models.CharField(max_length=30)