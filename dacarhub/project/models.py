from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class car(models.Model):
    image = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    maker = models.CharField(max_length = 50)
    type = models.CharField(max_length = 50)
    mileage = models.CharField(max_length = 50)
    year = models.CharField(max_length = 50)
    price = models.IntegerField()

