# Generated by Django 5.0.1 on 2024-01-22 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_alter_user_create_at_alter_user_update_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True, default=None, null=True, upload_to="images"
            ),
        ),
    ]