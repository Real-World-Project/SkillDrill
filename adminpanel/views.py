from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, DeleteView, ListView, DetailView, CreateView
from django.views.generic.edit import *
from blog.models import Post
from locations.models import Location, Services, Category, Order
from customers.models import Customer
from django.urls import reverse_lazy


# # Create your views here.
class dashboardView(ListView):
    model = Order
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

class blogUpdateView(UpdateView):
    model = Post
    template_name = 'weblog/edit_blog.html'
    fields = '__all__'
    success_url = reverse_lazy('weblog')


class blogDeleteView(DeleteView):
    model = Post
    template_name = 'weblog/blog_delete.html'
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

class serviceUpdateView(UpdateView):
    model = Services
    template_name = 'webservice/edit_service.html'
    fields = '__all__'
    success_url = reverse_lazy('webservice')


class serviceDeleteView(DeleteView):
    model = Services
    template_name = 'webservice/service_delete.html'
    success_url = reverse_lazy('webservice')


class weborderView(ListView):
    model = Order
    template_name = 'weborder/weborder.html'

class AddOrderView(CreateView):
    model = Order
    template_name = 'weborder/add_order.html'
    fields = '__all__'

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'weborder/edit_order.html'
    fields = '__all__'
    success_url = reverse_lazy('weborder')


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'weborder/order_delete.html'
    success_url = reverse_lazy('weborder')



class adminaccountView(TemplateView):
    template_name = 'account/account.html'


def count(request):
    posts = Post.objects.all()
    post_count = posts.count()

    locations = Location.objects.all()
    location_count = locations.count()
    services = Services.objects.all()
    service_count = services.count()
    customers = Customer.objects.all()
    customer_count = customers.count()
    # customer_count = customer.filter(is_staff=0).count()
    # superuser_count = customer.filter(is_staff=1).count()
    context = {
        'post_count': post_count,
        'location': location_count,
        'service': service_count,
        'customer': customer_count,
        # 'admin': superuser_count,

    }
    return render(request, 'adminpanel/dashboard.html', context)
