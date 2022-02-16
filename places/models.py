from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название места")
    description_short = models.TextField(blank=True, verbose_name="Краткое описание")
    description_long = HTMLField(blank=True, verbose_name="Полное описание")
    lng = models.DecimalField(max_digits=20, decimal_places=16, verbose_name="Долгота")
    lat = models.DecimalField(max_digits=20, decimal_places=16, verbose_name="Широта")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"


class Image(models.Model):
    img = models.ImageField(verbose_name="Изображение")
    place = models.ForeignKey("Place", on_delete=models.CASCADE, related_name="images", verbose_name="Место")
    order = models.IntegerField(verbose_name="Порядок", blank=True, default=0)

    def __str__(self):
        return f"{self.order} {self.place.title}"

    class Meta:
        ordering = ["order"]
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
