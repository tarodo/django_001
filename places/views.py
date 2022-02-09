from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from places.models import Place


def get_place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    imgs = [img.img.url for img in place.images.all()]
    place_front_style = {
        "title": place.title,
        "imgs": imgs,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {"lng": place.lng, "lat": place.lat},
    }
    return JsonResponse(
        place_front_style, json_dumps_params={"indent": 2, "ensure_ascii": False}
    )


def show_homepage(request):
    all_points = Place.objects.all()
    features = []
    for point in all_points:
        features.append(
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [point.lng, point.lat]},
                "properties": {
                    "title": point.title,
                    "placeId": point.id,
                    "detailsUrl": f"/places/{point.id}",
                },
            }
        )

    map_points = {"type": "FeatureCollection", "features": features}

    data = {"map_points": map_points}
    return render(request, "homepage.html", context=data)
