from django.shortcuts import render
from .models import Location, Services

# Create your views here.

def location(request, location_name): #, service_id
    locations = Location.objects.get(location=location_name)
    # services = Services.objects.all() #get(id=service_id)
    return render(request, "locations/location.html",{
        "locations":locations, "services":locations.services.all()
    })

# Create your views here.
