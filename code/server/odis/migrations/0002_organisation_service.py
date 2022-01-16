# Generated by Django 4.0.1 on 2022-01-09 16:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("odis", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Organisation",
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
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("cts", models.DateTimeField(auto_now_add=True)),
                ("uts", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=128, unique=True)),
                ("url", models.CharField(max_length=256, unique=True)),
                ("logo", models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Service",
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
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("cts", models.DateTimeField(auto_now_add=True)),
                ("uts", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=128, unique=True)),
                ("url", models.CharField(max_length=256, unique=True)),
                (
                    "audience_type",
                    models.CharField(blank=True, max_length=32, null=True),
                ),
                (
                    "audience_administrative_area_name",
                    models.CharField(blank=True, max_length=64, null=True),
                ),
                ("category", models.CharField(blank=True, max_length=64, null=True)),
                ("description", models.TextField()),
                ("logo", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "provider",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="odis.organisation",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
