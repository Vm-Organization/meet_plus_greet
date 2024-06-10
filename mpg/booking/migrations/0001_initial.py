# Generated by Django 5.0.6 on 2024-06-10 08:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('airport', '0001_initial'),
        ('main_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_status', models.CharField(choices=[('unpaid', 'Не оплачен'), ('paid', 'Оплачен'), ('confirmed', 'Подтвержден'), ('cancelled', 'Отменен')], default='unpaid', max_length=100)),
                ('flight_number', models.CharField(max_length=100)),
                ('departure_datetime', models.DateTimeField()),
                ('arrival_datetime', models.DateTimeField()),
                ('passenger_number', models.PositiveIntegerField()),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('telegram', models.CharField(blank=True, max_length=100, null=True)),
                ('total_price', models.CharField(max_length=50, null=True)),
                ('arrival_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_booking', to='airport.airport')),
                ('arrival_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_service', to='main_app.serviceprice')),
                ('arrival_terminal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_booking', to='airport.terminal')),
                ('departure_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_booking', to='airport.airport')),
                ('departure_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_service', to='main_app.serviceprice')),
                ('departure_terminal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_booking', to='airport.terminal')),
                ('transit_airport', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transit_booking', to='airport.airport')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PassengerBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passenger_booking', to='booking.booking')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passenger_booking', to='main_app.passenger')),
            ],
        ),
    ]
