from django.db import models

# Create your models here.


class Menu(models.Model):
    title = models.CharField(max_length=20)
    price = models.IntegerField()
    descr = models.TextField(blank=True)
    image = models.CharField(max_length=30)
