# Generated by Django 4.1 on 2022-08-31 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
        ("querier", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scannedpackages",
            name="client_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="authentication.client"
            ),
        ),
    ]