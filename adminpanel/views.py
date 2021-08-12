from django.shortcuts import render
from django.views.generic import *
from django.views.generic.edit import *
from blog.models import Post
from locations.models import Location, Services, Category

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
    template_name = 'weblog/Create_New_Blog.html'
    fields = '__all__'

class weblocationView(ListView):
    model = Location
    template_name = 'weblocation/weblocation.html'

class AddLocationView(CreateView):
    model = Location
    template_name = 'weblocation/Add_Location.html'
    fields = '__all__'

class DetailLocationView(DetailView):
    model = Location
    template_name = "weblocation/location_view.html"

class LocationUpdateView(UpdateView):
    model = Post
    template_name = 'weblocation/Edit_Location.html'
    fields = ['location', 'cover']

class webserviceView(ListView):
    model = Services
    template_name = 'webservice/webservice.html'

class AddServiceView(CreateView):
    model = Services
    template_name = 'webservice/Add_Services.html'
    fields = '__all__'

class adminaccountView(TemplateView):
    template_name = 'account/account.html'





