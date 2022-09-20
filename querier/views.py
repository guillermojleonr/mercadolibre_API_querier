from django.shortcuts import render, redirect
from .forms import SearchForm
from .models import ScannedPackages
from querier.querier import ClientQuerier
import json

def querier_view(request):
    search_form = SearchForm() # Set Unbound form
    
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
            for tuple in list_of_tuples:
                data = ScannedPackages(shipment_id=tuple[0],client_id_id=tuple[1])
                data.save()
            
            return redirect("/querier/querier/?valid")
        else:
            return redirect("/querier/querier/?error")
    
    return render(request, "querier/search.html",{"search_form":search_form})

def querier_update_shipment_view(request):
    cq = ClientQuerier()
    cq.add_new_shipment_info_to_db()
    
    return render(request, "querier/search.html")
