# Generated by Django 4.2.13 on 2024-06-04 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("onlineshop", "0020_newsarticle"),
    ]

    operations = [
        migrations.CreateModel(
            name="FAQ",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.CharField(max_length=255)),
                ("answer", models.TextField()),
                ("date_added", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]