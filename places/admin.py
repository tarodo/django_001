from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from places.models import Image, Place


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["place_preview"]
    fields = ("img", "place_preview", "order")

    def place_preview(self, obj):
        return format_html('<img src="{}" height="200px" />', obj.img.url)


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ("place",)


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image, ImageAdmin)
