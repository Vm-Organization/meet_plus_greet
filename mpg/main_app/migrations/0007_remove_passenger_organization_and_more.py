# Generated by Django 5.0.6 on 2024-06-07 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_passenger_additional_info_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='passenger',
            name='passport',
        ),
    ]