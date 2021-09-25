from django.urls import path
from .views import *


urlpatterns = [

    path('register/', createProfessional.as_view(), name='register_professional'),
    path('signin/', professionalLogin.as_view(), name='signin_professional'),
    # path('view_order/', view_Order, name='view_order_professional'),
    path('professionalLogout/', professionalLogout, name='professionalLogout'),
    path('<str:professional_email>/', view_Order, name='view_order_professional'),

]
