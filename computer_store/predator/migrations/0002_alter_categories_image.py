# Generated by Django 5.0.1 on 2024-01-22 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("predator", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categories",
            name="image",
            field=models.ImageField(
                blank=True, default=None, null=True, upload_to="images"
            ),
        ),
    ]
