# Generated by Django 5.0.6 on 2024-06-14 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_account_phone_alter_passenger_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprice',
            name='service_type',
            field=models.CharField(choices=[('arrival', 'Прибытие'), ('departure', 'Отправление'), ('transit', 'Транзит')], max_length=100),
        ),
    ]