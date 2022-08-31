from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def user_logout_view(request):
    logout(request)

    return redirect('main')

def user_login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('main')
            else:
                messages.error(request, "usuario no válido")
        else:
            messages.error(request, "información incorrecta")

    form=AuthenticationForm()
    return render(request,"user_authentication/user_login.html",{"form":form})




    

        
