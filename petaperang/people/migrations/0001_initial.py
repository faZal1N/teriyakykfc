# Generated by Django 4.2.7 on 2023-11-03 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("maps", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Person",
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
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField(unique=True)),
                ("biography", models.TextField(blank=True)),
                ("photo", models.ImageField(upload_to="personalities")),
                ("events", models.ManyToManyField(blank=True, to="maps.event")),
            ],
            options={
                "db_table": "person",
            },
        ),
    ]
