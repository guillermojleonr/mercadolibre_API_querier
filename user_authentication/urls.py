from django.urls import path

from .views import *

urlpatterns = [
    path('user_logout/',user_logout_view, name="user_logout"),
    path('user_login/',user_login_view, name="user_login"),
]



