from multiprocessing.connection import Client
from django.db import models
from authentication.models import Client

# Create your models here.

class ScannedPackages(models.Model):
    shipment_id = models.CharField(max_length=50)
    client_id = models.ForeignKey(Client, on_delete=models.PROTECT)

    class Meta:
        verbose_name="scanned package"
        verbose_name_plural="scanned packages"

    def __str__(self):
        return self.shipment_id + ' ' + self.client_id