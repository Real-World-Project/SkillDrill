from django.shortcuts import render, redirect
from django.views.generic import *
from .models import Professional
from locations.models import Order
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import  check_password



# Create your views here.
class createProfessional(View):
    def get(self, request):
        return render(request, "signup1.html")

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message= None

        professional = Professional(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateProfessional(professional)


        if not error_message:
            print(first_name, last_name, phone, email, password)
            professional.password = make_password(professional.password)
            professional.save()
            return redirect('home')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'professionals/professionalSignup.html', data)

    def validateProfessional(self, professional):
        error_message = None;
        if (not professional.first_name):
            error_message = "First Name Required !!"
        elif len(professional.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not professional.last_name:
            error_message = 'Last Name Required'
        elif len(professional.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not professional.phone:
            error_message = 'Phone Number required'
        elif len(professional.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(professional.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(professional.email) < 5:
            error_message = 'Email must be 5 char long'
        elif professional.isExists():
            error_message = 'Email Address Already Registered..'
        # saving
        return error_message



class professionalLogin(View):
    return_url= None
    def get(self, request):
        professionalLogin.return_url = request.GET.get('return_url')
        return render(request, 'professionals/professionalSignin.html')


    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        professional =Professional.get_professional_by_email(email)
        error_message = None
        if professional:
            flag = check_password(password, professional.password)
            if flag:
                request.session['professional']= professional.id
                if professionalLogin.return_url:
                    return HttpResponseRedirect(professionalLogin.return_url)
                else:
                    professionalLogin.return_url = None
                    return redirect('view_order_professional')
            else:
                error_message= 'Email or Password Invalid'
        else:
            error_message = 'Email or Password invalid'
        return render(request, 'professionals/professionalSignin.html', {'error': error_message})

def professionalLogout(request):
    request.session.clear()
    return redirect('home')

# class view_Order(ListView):
#     model = Order
#     template_name='professionals/View_Order.html'
#     fields = '__all__'

def view_Order(request, professional_email):  # service_id
    professional = Professional.objects.get(email= professional_email)
    print(professional)
    order = professional.prof_serv.all()
    orders = Order.objects.all()
    return render(request, "professionals/View_Order.html", {
        "order": order,
        "orders": orders
    })