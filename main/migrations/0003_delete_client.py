# Generated by Django 4.1 on 2022-08-31 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_client_created_client_updated"),
    ]

    operations = [
        migrations.DeleteModel(name="Client",),
    ]
