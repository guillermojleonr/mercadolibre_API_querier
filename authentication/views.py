from django.shortcuts import render
from app import app
from django.conf import settings
from .models import Client, Tokens
# Create your views here.


def login_view(request):
    return render(request, "authentication/login.html")

def redirect_view(request):
    get = request.GET
    code = get.__getitem__('code')
    app_instance = app()
    tokens = app_instance.exchange_code_to_token(code)
    user_id = tokens['user_id']
    clients = app_instance.add_clients_info(user_id,tokens)
    return render(request, "authentication/redirect.html")