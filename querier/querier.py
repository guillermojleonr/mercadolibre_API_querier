from main.app import *
from authentication.models import *
from querier.models import *
from datetime import datetime, timezone
from custom_exceptions import myError

class ClientQuerier(Client,app):
    """ 
    Purpose: Perform the "querier" functionality
    """
 
    def refresh_tokens(self,refresh_token):

        """ 
        Purpose: Updates tokens and returns a dictionary with the new tokens 
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

    def get_shipment(self,access_token,shipment_id):

        """ 
        Purpose: Gets the shipment info.
        
        """

        url = f"https://api.mercadolibre.com/shipments/{shipment_id}"
        payload={}
        headers = {
        'Authorization': f'Bearer {access_token}',
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        response_dictionary = json.loads(response.text)
        return response_dictionary

    def get_client_info(self,user_id, access_token):

        """ 
        Purpose: Get the client info
        API Resource: $ curl -X GET -H 'Authorization: Bearer $ACCESS_TOKEN' https://api.mercadolibre.com/users/{User_id} 
        """

        url = f"https://api.mercadolibre.com/users/{user_id}"
        payload={}
        headers = {
        'Authorization': f'Bearer {access_token}',
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        response_dictionary = json.loads(response.text)
        return response_dictionary
            
    def check_lifespan_access_token(self,passed_access_token):

        """ 
        Purpose: Returns the time difference between the last tokens update and the current time, if the time difference is greater than 21600 seconds, 
        the tokens should be refreshed with Client.Querier.refresh_tokens() method.

        Input: Access token to be evaluated.

        Output: Access token timespan in seconds. 
        """

        tks = Tokens.objects.filter(access_token=passed_access_token)
        
        for token in tks:
            access_token_updated = token.updated
            current_datetime = datetime.now(timezone.utc)
            time_difference = (current_datetime - access_token_updated).total_seconds()

        return time_difference
    
    def update_tokens_to_db(self,tokens_dict):
        """ 
        Purpose: updates new tokens to the db.

        Input: Dictionary object containing the user_id and the new fresh tokens.

        Output: Tuple containing the query object and  confirmation if the create operation is succesfull.
        """
        user_id = tokens_dict['user_id']
        access_token = tokens_dict['access_token']
        refresh_token = tokens_dict['refresh_token']
        
        (obj, created) = Tokens.objects.update_or_create(
        client_id_id = user_id,
        defaults={'refresh_token':refresh_token,'access_token':access_token,'updated':datetime.now(timezone.utc)}
        )
        return (obj,created)
    
    def update_shipment_info_to_db(self,shipment_info):

        """ 
        Purpose: updates shipment additional info to the db: receiver name, receiver address and receiver phone

        Input: Dictionary object containing the the shipment information

        Output: Tuple containing the query object and confirmation if create operation is succesfull.
        """
        sender_id = shipment_info["sender_id"]
        id = shipment_info["id"]
        receiver_address = shipment_info["receiver_address"]["address_line"]
        receiver_name = shipment_info["receiver_address"]["receiver_name"]
        receiver_phone = shipment_info["receiver_address"]["receiver_phone"]
        
        (obj, created) = ScannedPackages.objects.update_or_create(
        shipment_id = id,
        defaults={'receiver_address':receiver_address,'receiver_name':receiver_name,'receiver_phone':receiver_phone}
        )
        
        return (obj,created)

    def add_new_shipment_info_to_db(self):

        """ Purpose: Iterates over all shipment records that doesn't have additional information and executes get_shipment and 
        update_shipment_info_to_db functions in order to store this new information in the DB """

        sp = ScannedPackages.objects.filter(receiver_address__isnull=True, receiver_name__isnull=True, receiver_phone__isnull=True) #queryset

        for shipment in sp:
            shipment_id = shipment.shipment_id
            client_id = shipment.client_id_id
            receiver_address = shipment.receiver_address #NULL by now
            receiver_name = shipment.receiver_name #NULL by now
            receiver_phone = shipment.receiver_phone #NULL by now

            #Checking if access_token is active
            tks = Tokens.objects.filter(client_id_id=client_id)
            
            for token in tks:  #Iteration over a 1-row queryset, I don't know how to get a queryset value  without iterating over it.
                access_token = token.access_token
                refresh_token = token.refresh_token
                access_token_lifespan = self.check_lifespan_access_token(access_token)

            if access_token_lifespan > 21600:
                new_tokens = self.refresh_tokens(refresh_token)
                token_update_operation = self.update_tokens_to_db(new_tokens)
                print(token_update_operation)
                shipment_info = self.get_shipment(access_token,shipment_id)

            else:
                shipment_info = self.get_shipment(access_token,shipment_id)
            
            #New shipment info is updated to db and result is printed, this operation should be logged somewhere.
            shipment_update_operation = self.update_shipment_info_to_db(shipment_info)
            print(shipment_update_operation)



