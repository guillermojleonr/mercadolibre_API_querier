from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('querier/',views.querier_view, name="querier"),
    path('querier_add_info/',views.querier_update_shipment_view, name="querier_update_shipment")
]