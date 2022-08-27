from django.db import models

# Create your models here

class Client(models.Model):
    name = models.CharField(max_length=50)
    client_id = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    authorization_token = models.CharField(max_length=50)
    refresh_token = models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="client"
        verbose_name_plural="clients"

    def __str__(self):
        return self.name