# Generated by Django 3.2 on 2021-04-17 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_merge_20210415_2245"),
    ]

    operations = [
        migrations.RenameField(
            model_name="offer",
            old_name="plataform",
            new_name="platform",
        ),
    ]
