from datetime import datetime, timezone

from django.conf import settings
from django.shortcuts import render

from main.app import *
from querier.querier import ClientQuerier

from .models import Client, Tokens


def login_view(request):
    app_instance = app()
    redirect_uri = app_instance.redirect_uri
    app_id = app_instance.app_id
    return render(request, "authentication/login.html",{"redirect_uri":redirect_uri,"app_id":app_id})

def redirect_view(request):
    # Object instances
    app_instance = app()
    client_instance = ClientQuerier()
    
    get = request.GET
    code = get.__getitem__('code')
    tokens = app_instance.exchange_code_to_token(code) #Returns user id, access and refresh tokens in a dictionary
    
    #Data by field
    user_id = tokens['user_id']
    access_token = tokens['access_token']
    refresh_token = tokens['refresh_token']

    #Gets the remaining client info
    client_info = client_instance.get_client_info(user_id,access_token) #Returns dictionary

    #Data by field
    client_nickname = client_info['nickname']
    client_name = client_info['first_name']

    #Create new client or get it if already exist.
    Client.objects.get_or_create(
    client_id = user_id,
    defaults={'name':client_name,'nickname':client_nickname},
    )

    #Create or update Tokens.
    Tokens.objects.update_or_create(
    client_id_id = user_id,
    defaults={'client_id_id':user_id,'refresh_token':refresh_token,'access_token':access_token,'updated':datetime.now(timezone.utc)}
    )
    
    return render(request, "authentication/redirect.html")