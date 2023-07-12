# Generated by Django 4.2.1 on 2023-06-26 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shopify", "0002_registration"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("pro_name", models.CharField(blank=True, max_length=150, null=True)),
                ("pro_image", models.ImageField(upload_to="")),
                ("pro_desc", models.CharField(blank=True, max_length=150, null=True)),
                ("pro_price", models.IntegerField()),
                (
                    "Category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shopify.category",
                    ),
                ),
            ],
        ),
    ]
