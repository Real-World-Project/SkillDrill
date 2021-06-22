from django.shortcuts import render
from .models import Location

# Create your views here.

def location(request, location_name):
    locations = Location.objects.get(location=location_name)
    return render(request, "locations/location.html",{
        "locations":locations
    })

# Create your views here.
