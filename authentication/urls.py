from django.urls import path
from . import views

urlpatterns = [
    
    path('login/',views.login_view, name="login"),
    path('redirect/',views.redirect_view, name="redirect"),
]