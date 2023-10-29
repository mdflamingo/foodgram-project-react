# Generated by Django 4.2.5 on 2023-10-29 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_follow"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="follow",
            constraint=models.UniqueConstraint(
                fields=("user", "following"), name="unique_user_following"
            ),
        ),
    ]
