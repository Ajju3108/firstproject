from django.db import models

# Create your models here.

class employee(models.Model):
    eno = models.IntegerField()
    name = models.CharField(max_length=30)
    esal = models.FloatField(max_length=30)
    eadr = models.CharField(max_length=30)