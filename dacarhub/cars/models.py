from django.db import models



class car(models.Model):
    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length = 50)
    maker = models.CharField(max_length = 50)
    type = models.CharField(max_length = 50)
    mileage = models.CharField(max_length = 50)
    year = models.CharField(max_length = 50)
    price = models.IntegerField()
    fuel = models.IntegerField()

