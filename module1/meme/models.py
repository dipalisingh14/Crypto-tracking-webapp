from django.db import models

# Create your models here.
class signup(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=50)
    checkbox = models.BooleanField()

class datacsv(models.Model):
    symbol=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    last_sale=models.FloatField()
    net_change=models.FloatField()
    #percentage_change=models.FloatField()
    country=models.CharField(max_length=1000)
    industry=models.CharField(max_length=10000)

