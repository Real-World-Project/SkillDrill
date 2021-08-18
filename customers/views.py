from django.shortcuts import render , redirect ,HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Customer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import  check_password
# Create your views here.


class Signup1(View):
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

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)


        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.save()
            return redirect('home')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup1.html', data)

    def validateCustomer(self, customer):
        error_message = None;
        if (not customer.first_name):
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif len(customer.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        # saving
        return error_message



# class Login1(View):
#     return_url = None
#     def get(self , request):
#         Login1.return_url = request.GET.get('return_url')
#         return render(request , 'login1.html')
#
#     def post(self , request):
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         customer = Customer.get_customer_by_email(email)
#         error_message = None
#         if customer:
#             flag = check_password(password, customer.password)
#             if flag:
#                 request.session['customer'] = customer.id
#
#                 if Login1.return_url:
#                     return HttpResponseRedirect(Login1.return_url)
#                 else:
#                     Login1.return_url = None
#                     return redirect('home')
#             else:
#                 error_message = 'Email or Password invalid !!'
#         else:
#             error_message = 'Email or Password invalid !!'
#
#         print(email, password)
#         return render(request, 'login1.html', {'error': error_message})
class login1(View):
    return_url= None
    def get(self, request):
        login1.return_url = request.GET.get('return_url')
        return render(request, 'login1.html')


    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer =Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer']= customer.id
                if login1.return_url:
                    return HttpResponseRedirect(login1.return_url)
                else:
                    login1.return_url = None
                    return redirect('home')
            else:
                error_message= 'Email or Password Invalid'
        else:
            error_message = 'Email or Password invalid'
        return render(request, 'Login1.html', {'error': error_message})

def logout1(request):
    request.session.clear()
    return redirect('home')
