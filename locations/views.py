from django.shortcuts import render, redirect
from .models import Location, Services, Category
# from django.views.generic import TemplateView
from django.views import View

# Create your views here.

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
    service = request.POST.get('services')
    remove = request.POST.get('remove')
    # request.session['services_id'] = services.id
    # request.session.get('cart').clear()
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}



    if cart:
        request.session.get('cart').clear()
        
        quantity = cart.get(service)
        if quantity:
            if remove:
                if quantity<=1:
                    cart.pop(service)
                else:
                    cart[service] = quantity-1
            else:

                cart[service] = quantity+1
        else:

            cart[service] = 1
    else:

        cart = {}
        cart[service] = 1

    request.session['cart'] = cart

    # print("this is id : ", request.session.get('services_id'))
    # print("this is cart : ", cart)
    print("**", request.session['cart'])

    return render(request, "locations/service.html", {
        "services": services, "locations": locations
    })


class CartView(View):
    # template_name = 'cart/cart.html'
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        services = Services.get_services_by_id(ids)
        print(services)
        return render(request, 'cart/cart.html', {'services':services})


class CheckoutView(View):
    def post(self, request):
        print(request.POST)
        return redirect("cart")
