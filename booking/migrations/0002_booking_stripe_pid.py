# Generated by Django 3.2.4 on 2021-08-30 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
