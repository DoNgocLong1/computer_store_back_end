# Generated by Django 5.0.1 on 2024-01-17 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True, default=None, null=True, upload_to="user/avatar/"
            ),
        ),
    ]
