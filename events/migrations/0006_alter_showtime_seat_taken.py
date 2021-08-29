# Generated by Django 3.2.4 on 2021-08-28 23:33

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_showtime_seat_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showtime',
            name='seat_taken',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=254), blank=True, default=list, null=True, size=None),
        ),
    ]
