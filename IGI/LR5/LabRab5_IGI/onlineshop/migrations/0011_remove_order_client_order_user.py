# Generated by Django 4.2.13 on 2024-05-30 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("onlineshop", "0010_alter_review_created_at_alter_review_rating_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="client",
        ),
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
