from django.db import models

# Create your models here.

# models.Model automatically assign id for item in column 1
class Item(models.Model):
    text = models.TextField(default='')


