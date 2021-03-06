# Generated by Django 3.2.4 on 2021-08-29 15:53

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('run_time', models.IntegerField()),
                ('description_short', models.TextField()),
                ('description_long', models.TextField()),
                ('image_hero', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_normal', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('capacity', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('seat_map', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=254), blank=True, default=list, null=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('ticket_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('seat_taken', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=254), blank=True, default=list, null=True, size=None)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.event')),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.venue')),
            ],
        ),
    ]
