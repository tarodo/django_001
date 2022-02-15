import io
from io import BytesIO

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from PIL import Image

from places.models import Image as ImageModel
from places.models import Place


def load_json(json_url: str):
    """Check file and load data from it"""
    response = requests.get(json_url)
    response.raise_for_status()
    place = response.json()

    new_place, _ = Place.objects.get_or_create(
        title=place["title"],
        defaults={"description_short": place["description_short"],
                  "description_long": place["description_long"],
                  "lng": place["coordinates"]["lng"],
                  "lat": place["coordinates"]["lat"]
                  }
    )
    for idx, img_link in enumerate(place["imgs"], start=1):
        response = requests.get(img_link)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG", quality=75)
        new_img = ImageModel(place=new_place, order=idx)
        new_img.img.save(f"img_{idx}.jpg", ContentFile(buffer.getbuffer()), save=True)


class Command(BaseCommand):
    """Load data"""

    help = "Load data from json"

    def handle(self, *args, **options):
        load_json(options["json"])

    def add_arguments(self, parser):
        parser.add_argument("-j", "--json", action="store", help="Путь до JSON файла")
