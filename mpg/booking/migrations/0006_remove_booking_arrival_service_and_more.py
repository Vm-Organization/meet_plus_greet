# Generated by Django 5.0.6 on 2024-06-14 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_remove_passengerbooking_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='arrival_service',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='departure_service',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='transit_service',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_status',
            field=models.CharField(choices=[('unpaid', 'Не оплачен'), ('paid', 'Оплачен'), ('confirmed', 'Подтвержден'), ('cancelled', 'Отменен'), ('completed', 'Завершен')], default='unpaid', max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='passenger_number',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
