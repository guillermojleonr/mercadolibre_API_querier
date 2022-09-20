""" 
Purpose: Define the authorization and authentication processes
"""
import requests
import json
from django.conf import settings

class app():
    
    def __init__(self):
        self.app_id = settings.APP_ID
        self.client_secret = settings.CLIENT_SECRET
        self.redirect_uri = "https://127.0.0.1:8000/authentication/redirect/"
    
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

class Developer():
    def create_test_user(access_token):
        """ 
        Purpose: create test users
        Comment: In order to create a user the access token must have read privileges in your app settings.
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