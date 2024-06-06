# Generated by Django 5.0.4 on 2024-06-06 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_alter_contact_message_alter_contact_phone"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
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
                    "number",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Номер версии"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Название"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Активность"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Версия",
                "verbose_name_plural": "Версии",
                "ordering": ["number"],
            },
        ),
    ]