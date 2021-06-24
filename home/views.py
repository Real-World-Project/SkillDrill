from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from locations.models import Location
from .forms import ContactForm
# Create your views here.


# def home(request):
#     return render(request,'home/home.html',{
#         "locations":Location.objects.all(),
#     })

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'skilldrillproject@gmail.com', ['skilldrillproject@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, "Message sent.")
            return redirect("home")

    form = ContactForm()
    return render(request, "home/home.html", {
        "locations": Location.objects.all(),'form': form} )