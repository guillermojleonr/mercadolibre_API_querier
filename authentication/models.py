from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50)
    client_id = models.CharField(max_length=50,unique=True)
    nickname = models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="client"
        verbose_name_plural="clients"

    def __str__(self):
        return self.name

class Tokens(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, to_field='client_id')
    refresh_token = models.CharField(max_length=50)
    access_token = models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)