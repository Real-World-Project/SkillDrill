from django.urls import path
from locations import views

urlpatterns = [
    path('<str:location_name>', views.location, name="location"),
    # path('<str:location_name>/<str:service_name>', views.service, name="service"),
    # path('<str:location_name>/<str:category_name>', views.category, name="categories"),
    # path('<str:location_name>/<str:category_name>/<str:service_name>', views.category, name="services"),
    path('<str:location_name>/<str:service_name>', views.service, name="service")

]
