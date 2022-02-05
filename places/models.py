from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=100)
    description_short = models.CharField(max_length=100)
    description_long = models.TextField()
    lng = models.DecimalField(max_digits=20, decimal_places=16)
    lat = models.DecimalField(max_digits=20, decimal_places=16)

    def __str__(self):
        return self.title


class Image(models.Model):
    img = models.ImageField()
    place = models.ForeignKey("Place", on_delete=models.CASCADE, related_name="images")
    order = models.IntegerField()

    def __str__(self):
        return f"{self.order} {self.place.title}"
