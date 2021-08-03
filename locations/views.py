from django.shortcuts import render
from .models import Location, Services, Category
from django.views import View

# Create your views here.

# class Index(View):
#     def post(self, request):
#         services = request.POST.get('product')
#         print(services)




def location(request, location_name):  # service_id
    locations = Location.objects.get(location=location_name)
    category = Category.objects.all()
    return render(request, "locations/location.html", {
        "locations": locations, "services": locations.services.all(), "category": category
    })


def category(request, category_name):
    category = Category.objects.get(title=category_name)
    return render(request, "locations/service.html", {
        "category": category
    })


def service(request, service_name, location_name):
    services = Services.objects.get(title=service_name)
    locations = Location.objects.get(location=location_name)
    request.session['services_id'] = services.id
    print("this is id : ", request.session.get('services_id'))
    return render(request, "locations/service.html", {
        "services": services, "locations": locations
    })
