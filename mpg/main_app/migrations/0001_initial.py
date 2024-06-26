# Generated by Django 5.0.6 on 2024-06-18 16:04

import django.db.models.deletion
import main_app.utils
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('airport', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True, validators=[main_app.utils.valid_phone_number])),
                ('personal_information', models.TextField(blank=True, null=True)),
                ('profile_configuration', models.JSONField(blank=True, null=True)),
                ('organization', models.CharField(blank=True, max_length=150, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('birth_date', models.DateField(validators=[main_app.utils.age_type])),
                ('age', models.CharField(choices=[('infant', 'Ребенок (0-2 лет)'), ('child', 'Ребенок (2-12 лет)'), ('adult', 'Взрослый')], max_length=100)),
                ('phone', models.CharField(blank=True, max_length=20, null=True, validators=[main_app.utils.valid_phone_number])),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('personal_data', models.CharField(blank=True, max_length=500, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passenger', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ServicePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('arrival', 'Прибытие'), ('departure', 'Отправление'), ('transit', 'Транзит')], max_length=100)),
                ('price_one_passenger', models.CharField(max_length=100)),
                ('price_others_passengers', models.CharField(max_length=100)),
                ('airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_price', to='airport.airport')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_price', to='main_app.service')),
            ],
        ),
    ]
