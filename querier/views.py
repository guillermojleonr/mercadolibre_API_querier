import json

from django.contrib.auth.models import User
from django.db.utils import IntegrityError, OperationalError
from django.shortcuts import redirect, render

from custom_exceptions import myError
from querier.querier import ClientQuerier

from .forms import SearchForm
from .models import FailedScannedPackages, ScannedPackages


def querier_view(request):
    search_form = SearchForm()
    
    if request.method=="POST":
        search_form=SearchForm(data=request.POST) # Set bound form
        if search_form.is_valid(): #Validation
            packages=search_form.cleaned_data["packages"] #Get the whole field input.

            packages=packages.split() #Split each line into a list of strings
            
            #Transform to a list of dictionaries
            list_of_dictionaries = []
            for string in packages:
                dict = json.loads(string)
                list_of_dictionaries.append(dict)
            
            #Get only sender_id and shipment_id
            list_of_tuples = []
            for dict in list_of_dictionaries:
                list_of_tuples.append((dict['id'], dict['sender_id']))

            #Send the data to the database
            ie=False
            user = User.objects.get(id=request.user.id)
            user_id= user.id
            for tuple in list_of_tuples:
                try:
                    data = ScannedPackages(shipment_id=tuple[0],client_id_id=tuple[1],user_id_id=user_id)
                    data.save()
                except IntegrityError:
                    data = FailedScannedPackages(shipment_id=tuple[0],client_id=tuple[1],user_id_id=user_id)
                    data.save()
                    ie = True
                    continue
                except OperationalError:
                    return redirect("/querier/querier/?databasemightbelocked")
            
            if ie:
                return redirect("/querier/querier/?integrity_error")
            else:
                return redirect("/querier/querier/?valid")
        else:
            return redirect("/querier/querier/?error")
    
    return render(request, "querier/search.html",{"search_form":search_form})

def querier_update_shipment_view(request):
    cq = ClientQuerier()
    cq.add_new_shipment_info_to_db()
    return querier_view(request)
