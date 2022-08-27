from django.shortcuts import render
# Create your views here.


def login_view(request):    
    return render(request, "authentication/login.html")

def redirect_view(request):    
    return render(request, "authentication/redirect.html")