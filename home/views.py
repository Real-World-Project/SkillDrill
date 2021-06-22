from django.shortcuts import render
from locations.models import Location
# Create your views here.


def home(request):
    return render(request,'home/home.html',{
        "locations":Location.objects.all()
    })
