# Generated by Django 3.2.4 on 2021-08-29 15:53

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('seat_number', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=254), default=list, size=None)),
                ('seat_id', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=254), default=list, size=None)),
                ('booking_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('showtime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.showtime')),
            ],
        ),
    ]
