from django.shortcuts import render, redirect
from .models import Location, Services, Category
# from django.views.generic import TemplateView
from django.views import View

class Checkout(View):
    def post(self, request):
        print(request.POST)
        return redirect('cart/')
