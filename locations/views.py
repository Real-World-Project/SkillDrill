from django.shortcuts import render
from .models import Location, Services

# Create your views here.

def location(request, location_name): #, service_id
    locations = Location.objects.get(location=location_name)
    # services = Services.objects.all() #get(id=service_id)
    return render(request, "locations/location.html",{
        "locations":locations, "services":locations.services.all()
    })


def service(request, service_name, location_name):
    services = Services.objects.get(title=service_name)
    locations = Location.objects.get(location=location_name)
    return render(request, "locations/service.html",{
        "services":services, "locations":locations
    })
# Create your views here.
