from django.urls import path
from locations import views

urlpatterns = [
    path('<str:location_name>', views.location, name="location"),
    # path('<str:service_name>', views.location, name="service")
]
