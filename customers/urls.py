from django.contrib import admin
from django.urls import path
from .views import Signup1, login1, logout1


urlpatterns=[
    path('Signup1', Signup1.as_view(), name='signup1'),
    # path('Login1', Login1.as_view(), name='login1'),
    path('login1', login1),
    path('logout1', logout1 , name='logout1'),
]