# Generated by Django 3.2.4 on 2021-08-24 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_showtime_seating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='showtime',
            old_name='seating',
            new_name='seating_plan',
        ),
    ]