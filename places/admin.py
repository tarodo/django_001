from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ["place_preview"]
    fields = ("img", "place_preview", "order")

    def place_preview(self, obj):
        return format_html(f'<img src="{obj.img.url}" height="200px" />')


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)
