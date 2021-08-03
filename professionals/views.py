from django.shortcuts import render

# Create your views here.

def profesignup(request):
    return render(request, 'professionals/professionalSignup.html')

def finalsignup(request):
    return render(request, 'professionals/SignUpPage.html')

def success(request):
    return render(request, 'professionals/successMessage.html')

def profile(request):
    return render(request, 'professionals/profile.html')

def detail(request):
    return render(request, 'professionals/details.html')