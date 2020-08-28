from django.db import models

# Create your models here.


class List(models.Model):
    pass

# models.Model automatically assign id for item in column 1
class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey('lists.List', on_delete=models.CASCADE,related_name = 'lists', default = None)
