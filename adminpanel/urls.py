from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboardView.as_view(), name='dashboard'),
    path('team/', teamView.as_view(), name='team'),
path('adminaccount/', adminaccountView.as_view(), name='adminaccount'),
    path('weblog/', weblogView.as_view(), name='weblog'),
    path("weblog/<int:pk>/", DetailPostView.as_view(), name="blog_views"),
    path('weblog/newweblog/', BlogCreateView.as_view(), name='add_blog'),
    path('weblog/update/<int:pk>/', blogUpdateView.as_view(), name='edit_blog'),
    path('weblog/delete/<int:pk>/', blogDeleteView.as_view(), name='blog_delete'),
    path('weblocation/', weblocationView.as_view(), name='weblocation'),
    path('weblocation/addlocation/', AddLocationView.as_view(), name='add_location'),
    path('weblocation/update/<int:pk>/', LocationUpdateView.as_view(), name='edit_location'),
    path('weblocation/delete/<int:pk>/', locationDeleteView.as_view(), name='location_delete'),
    path("location/<int:pk>/", DetailLocationView.as_view(), name="location_view"),
    path('webservice/', webserviceView.as_view(), name='webservice'),
    path('webservice/addservice/', AddServiceView.as_view(), name='add-service'),
    path('webservice/update/<int:pk>/', serviceUpdateView.as_view(), name='edit_service'),
    path('webservice/delete/<int:pk>/', serviceDeleteView.as_view(), name='service_delete'),

]

