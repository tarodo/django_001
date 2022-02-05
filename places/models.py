from django.db import models


# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=100)
    description_short = models.CharField(max_length=100)
    description_long = models.TextField()
    lng = models.DecimalField(max_digits=20, decimal_places=16)
    lat = models.DecimalField(max_digits=20, decimal_places=16)

    def __str__(self):
        return self.title