# Generated by Django 5.0.1 on 2024-01-22 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("predator", "0002_alter_categories_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="categories", old_name="create_at", new_name="created_at",
        ),
        migrations.RenameField(
            model_name="categories", old_name="update_at", new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="order", old_name="create_at", new_name="created_at",
        ),
        migrations.RenameField(
            model_name="order", old_name="update_at", new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="orderitem", old_name="create_at", new_name="created_at",
        ),
        migrations.RenameField(
            model_name="orderitem", old_name="update_at", new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="product", old_name="create_at", new_name="created_at",
        ),
        migrations.RenameField(
            model_name="product", old_name="update_at", new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="productimages", old_name="create_at", new_name="created_at",
        ),
        migrations.RenameField(
            model_name="productimages", old_name="update_at", new_name="updated_at",
        ),
    ]