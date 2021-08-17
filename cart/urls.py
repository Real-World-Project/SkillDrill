from django.urls import path
from locations.views import CartView, CheckoutView

urlpatterns = [
    path('', CartView.as_view(), name="cart"),
    path('checkout', CheckoutView.as_view(), name="checkout"),

]
