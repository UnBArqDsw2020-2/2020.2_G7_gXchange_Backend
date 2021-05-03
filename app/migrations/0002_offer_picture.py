# Generated by Django 3.1.7 on 2021-03-30 23:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Offer",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("game_name", models.CharField(max_length=200)),
                ("plataform", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
                ("description", models.TextField()),
                ("is_valid", models.BooleanField(default=True)),
                ("date", models.DateField()),
                ("cep", models.CharField(max_length=50)),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("condition", models.IntegerField(choices=[(1, "New"), (2, "Seminew"), (3, "Used")])),
                ("email", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="Picture",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("bin", models.BinaryField()),
                ("id_offer", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="app.offer")),
            ],
        ),
    ]
