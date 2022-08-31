""" 
Module: auth
Purpose: Define the authorization and authentication processes
"""
import requests
import json
from django.conf import settings

clients = settings.CLIENTS

class app():
    
    def __init__(self):
        self.app_id = settings.APP_ID
        self.client_secret = settings.CLIENT_SECRET
        self.redirect_uri = "https://127.0.0.1:8000/authentication/redirect/"
    
    def get_auth_code(self):
        app_id = self.app_id
        redirect_uri = self.redirect_uri

        """ 
        Purpose: Get authentication code
        Comment: Currently not working, you need to browse return url in order to authenticate in the browser, then tobe redirected to the redirect_uri and be able to access the authentication code in the URL
        """
        url = f"https://auth.mercadolibre.cl/authorization?response_type=code&client_id={app_id}&redirect_uri={redirect_uri}"
        return url
    
    def exchange_code_to_token(self,code):
        """
        Purpose: Exchanges authentication code to get authorization tokens
        Output: a dictionary containing the JSON response
        """
        app_id = self.app_id
        client_secret = self.client_secret
        redirect_uri = self.redirect_uri
        url = "https://api.mercadolibre.com/oauth/token"

        payload=f'grant_type=authorization_code&client_id={app_id}&client_secret={client_secret}&code={code}&redirect_uri={redirect_uri}'

        headers = {
            'accept': 'application/json',
            'content-type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        response_dictionary = json.loads(response.text)
        return response_dictionary
    
    def refresh_tokens(self,refresh_token):
        """ 
        Purpose: refresh the tokens, uses the refresh token stored in the dictionary previously populated. To persist this data we need to encrypt it and store it in
        some persistent storage, query it and then use the refresh token as a parameter in this function
        """

        app_id = self.app_id
        client_secret = self.client_secret
        url = "https://api.mercadolibre.com/oauth/token"

        payload=f'grant_type=refresh_token&client_id={app_id}&client_secret={client_secret}&refresh_token={refresh_token}'
        
        headers = {
            'accept': 'application/json',
            'content-type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        response_dictionary = json.loads(response.text)
        return response_dictionary
    
    def create_test_user(access_token):
        """ 
        Purpose: create test users
        Comment: In order to create a user the access token must have read privileges, meaning that the app must have configured this option.
        """
        url = "https://api.mercadolibre.com/users/test_user"

        payload = json.dumps({
            "site_id": "MLC"
        })
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)

    def get_shipment(self,access_token,shipment_id):
        url = f"https://api.mercadolibre.com/shipments/{shipment_id}"
        payload={}
        headers = {
        'Authorization': f'Bearer {access_token}',
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        return response.text

    def get_shipments():
        #This function is supposed to update the ScannedPackages table to add the new fields such as
        #receiver_name, receiver_address, receiver_phone.
        #To do so this function must check if the 
        pass

    def add_clients_info(self,user_id,user_info):
        user_id_count = 0
        global clients
        for client in clients:
            if str(user_id) == client['user_id']:
                client['user_info'] = user_info
                user_id_count += 1
        else:
            print("empty list")
        
        if user_id_count == 0:
            clients.append({'user_id':user_id, 'user_info':user_info})
        return clients
            






""" #How to get authentication and authorization tokens
aplication = app() #Instance
print(aplication.get_auth_code()) #Get authentication url """

#Get the tokens in a dictionary
""" tokens = aplication.exchange_code_to_token("TG-62f571537ab41e00013bfb46-297131330") #Pass the auth code in params"""

#Refresh the tokens
""" refreshed_tokens = aplication.refresh_tokens(tokens["refresh_token"]) """