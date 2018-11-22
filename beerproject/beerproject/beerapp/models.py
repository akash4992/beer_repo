from django.db import models

# Create your models here.
class BeerBar(models.Model):
    bno = models.IntegerField()
    bname = models.CharField(max_length=70)
    color = models.CharField(max_length=70)
    bloc = models.CharField(max_length=70)
    alcholic = models.CharField(max_length=80)

