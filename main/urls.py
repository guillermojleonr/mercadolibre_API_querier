from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_view, name="main"),
    path('generic/',views.generic_view, name="generic"),
    path('elements/',views.elements_view, name="elements"),
    path('test/',views.testing_view),
]