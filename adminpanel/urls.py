from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboardView.as_view(), name='dashboard'),
    path('team/', teamView.as_view(), name='team'),
    path('weblog/', weblogView.as_view(), name='weblog'),
    path("<int:pk>/", DetailPostView.as_view(), name="blog_view"),
    path('adminaccount/', adminaccountView.as_view(), name='adminaccount'),
    path('weblog/newweblog/', BlogCreateView.as_view(), name='newweblog'),
    path('weblocation/', weblocationView.as_view(), name='weblocation'),
    path('weblocation/addlocation/', AddLocationView.as_view(), name='add-location'),
    path('location/<int:pk>/edit/', LocationUpdateView.as_view(), name='edit-location'),
    path("location/<int:pk>/", DetailLocationView.as_view(), name="location_view"),
    path('webservice/', webserviceView.as_view(), name='webservice'),
    path('webservice/addservice/', AddServiceView.as_view(), name='add-service'),
]

