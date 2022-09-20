from multiprocessing.connection import Client
from django.db import models
from authentication.models import Client
from main.app import *

# Create your models here.

class ScannedPackages(models.Model):
    shipment_id = models.CharField(max_length=50)
    client_id = models.ForeignKey(Client, on_delete=models.PROTECT, to_field='client_id')
    receiver_name = models.CharField(max_length=50, null=True)
    receiver_phone = models.CharField(max_length=50, null=True)
    receiver_address = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name="scanned package"
        verbose_name_plural="scanned packages"

    def __str__(self):
        return self.shipment_id

""" class Packgs(models.Model):
    receiver_name = models.CharField(max_length=50)
    receiver_phone = models.CharField(max_length=50)
    receiver_address = models.CharField(max_length=50)
    client_id = models.ForeignKey(ScannedPackages, on_delete=models.PROTECT, to_field='client_id_id')
    shipment_id = models.ForeignKey(ScannedPackages, on_delete=models.PROTECT, to_field='shipment_id')

    class Meta:
        verbose_name="package"
        verbose_name_plural="packages"

    def __str__(self):
        return self.shipment_id + ' ' + self.client_id + ' ' + self.receiver_name + ' ' + self.receiver_address """