from django.shortcuts import render
from .models import Location, Services, Category

# Create your views here.

# def location(request, location_name): #, service_id
#     locations = Location.objects.get(location=location_name)
#     category = Category.objects.all()
#     return render(request, "locations/location.html",{
#         "locations":locations, "services":locations.services.all(), "category":category
#     })

def location(request, location_name): #, service_id
    locations = Location.objects.get(location=location_name)
    category = Category.objects.all()
    return render(request, "locations/location.html",{
        "locations":locations, "services":locations.services.all(), "category":locations.services.all()
    })

def category(request, category_name):
    category = Category.objects.get(title=category_name)
    return render(request, "locations/service.html", {
        "category":category
    })

def service(request, service_name, location_name):
    services = Services.objects.get(title=service_name)
    locations = Location.objects.get(location=location_name)
    return render(request, "locations/service.html",{
        "services":services, "locations":locations
    })
