# Generated by Django 4.1.1 on 2022-10-01 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
