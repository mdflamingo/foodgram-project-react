# Generated by Django 4.2.5 on 2023-10-10 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("recipes", "0002_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ingredients", options={"ordering": ("name",)},
        ),
        migrations.RemoveField(model_name="cookingrecipe", name="image",),
        migrations.AlterField(
            model_name="cookingrecipe",
            name="author",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recipe",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
