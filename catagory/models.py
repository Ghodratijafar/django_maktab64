from django.db import models


# Create your models here.
class Catagory(models.Model):
    title = models.CharField(max_length=30)
    root = models.CharField(max_length=30)

    # def __str__(self):
    #     return f"title:{self.title}\nroot:{self.root}"
