from django.urls import path
from .views import location, service, CartView #, Checkout
from .checkout import Checkout

urlpatterns = [
    path('<str:location_name>', location, name="location"),
    # path('<str:location_name>/<str:service_name>', views.service, name="service"),
    # path('<str:location_name>/<str:category_name>', views.category, name="categories"),
    # path('<str:location_name>/<str:category_name>/<str:service_name>', views.category, name="services"),
    path('<str:location_name>/<str:service_name>', service, name="service"),
    path('cart/', CartView.as_view(), name="cart"),
    path('checkout', Checkout.as_view(), name="checkout"),

]
