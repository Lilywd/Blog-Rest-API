# Generated by Django 5.0.1 on 2024-01-24 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Posts", "0002_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="body",
            new_name="content",
        ),
    ]
