# Generated by Django 4.1.1 on 2022-10-11 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0004_post_customer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="customer",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="base.customer",
            ),
        ),
    ]
