from django.shortcuts import render

# Create your views here.

def profesignup(request):
    return render(request, 'professionals/professionalSignup.html')

def finalsignup(request):
    return render(request, 'professionals/SignUpPage.html')