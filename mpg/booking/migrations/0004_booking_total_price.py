# Generated by Django 5.0.6 on 2024-06-03 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_remove_booking_passenger_age_passengerbooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='total_price',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
