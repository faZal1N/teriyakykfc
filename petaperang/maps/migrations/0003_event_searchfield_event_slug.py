# Generated by Django 4.2.7 on 2023-11-04 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maps", "0002_event_x_event_y"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="searchfield",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="event",
            name="slug",
            field=models.SlugField(default=0, unique=True),
            preserve_default=False,
        ),
    ]
