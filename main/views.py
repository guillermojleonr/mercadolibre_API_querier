from django.conf import settings
from django.shortcuts import render
import logging

# Create your views here.

def main_view(request):    
    return render(request, "main/index.html")

def generic_view(request):    
    return render(request, "main/generic.html")

def elements_view(request):    
    return render(request, "main/elements.html")

def testing_view(request):
    sample_logger = logging.getLogger("sample_logger")
    
    sample_logger.debug('This is a sample message')
    print(settings.DEVELOPMENT_MODE)
    print(settings.DEBUG)
    return render(request, "main/index.html")