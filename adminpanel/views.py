from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, DeleteView, ListView, DetailView, CreateView
from django.views.generic.edit import *
from blog.models import Post
from locations.models import Location, Services, Category
from django.urls import reverse_lazy


# Create your views here.
class dashboardView(TemplateView):
    template_name = 'adminpanel/dashboard.html'


class teamView(TemplateView):
    template_name = 'team/team.html'


class weblogView(ListView):
    model = Post
    template_name = 'weblog/weblog.html'


class DetailPostView(DetailView):
    model = Post
    template_name = "weblog/blog_view.html"


class BlogCreateView(CreateView):
    model = Post
    template_name = 'weblog/add_blog.html'
    fields = '__all__'
    success_url = reverse_lazy('weblog')


class weblocationView(ListView):
    model = Location
    template_name = 'weblocation/weblocation.html'


class AddLocationView(CreateView):
    model = Location
    template_name = 'weblocation/add_location.html'
    fields = '__all__'


class DetailLocationView(DetailView):
    model = Location
    template_name = "weblocation/location_view.html"


class LocationUpdateView(UpdateView):
    model = Location
    template_name = 'weblocation/edit_location.html'
    fields = '__all__'
    success_url = reverse_lazy('weblocation')


class locationDeleteView(DeleteView):
    model = Location
    template_name = 'weblocation/location_delete.html'
    success_url = reverse_lazy('weblocation')


class webserviceView(ListView):
    model = Services
    template_name = 'webservice/webservice.html'


class AddServiceView(CreateView):
    model = Services
    template_name = 'webservice/Add_Services.html'
    fields = '__all__'


class adminaccountView(TemplateView):
    template_name = 'account/account.html'


class blogUpdateView(UpdateView):
    model = Post
    template_name = 'weblog/edit_blog.html'
    fields = '__all__'
    success_url = reverse_lazy('weblog')


class blogDeleteView(DeleteView):
    model = Post
    template_name = 'weblog/blog_delete.html'
    success_url = reverse_lazy('weblog')




