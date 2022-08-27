from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('querier/',views.querier_view, name="querier"),
]