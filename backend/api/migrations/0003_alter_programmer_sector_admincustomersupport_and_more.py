# Generated by Django 5.0.6 on 2024-06-09 22:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_programmer_categories_alter_programmer_sector"),
    ]

    operations = [
        migrations.AlterField(
            model_name="programmer",
            name="sector",
            field=models.CharField(
                choices=[
                    ("webdeveloper", "WebDeveloper"),
                    ("backenddeveloper", "BackendDeveloper"),
                    ("networking", "Networking"),
                    ("ai/machinelearning", "AI/MachineLearning"),
                    ("cloudservices", "CloudServices"),
                    ("admincustomersupport", "AdminCustomerSupport"),
                ],
                default="AI/MachineLearning",
                max_length=50,
            ),
        ),
        migrations.CreateModel(
            name="AdminCustomerSupport",
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
                (
                    "programmer",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="api.programmer"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BackEndDeveloper",
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
                (
                    "programmer",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="api.programmer"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CloudServices",
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
                (
                    "programmer",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="api.programmer"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MachineLearning",
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
                (
                    "programmer",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="api.programmer"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Networking",
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
                (
                    "programmer",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="api.programmer"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WebDeveloper",
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
                (
                    "programmer",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="api.programmer"
                    ),
                ),
            ],
        ),
    ]