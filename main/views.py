from django.shortcuts import render
# Create your views here.

def main_view(request):    
    return render(request, "main/index.html")

def generic_view(request):    
    return render(request, "main/generic.html")

def elements_view(request):    
    return render(request, "main/elements.html")