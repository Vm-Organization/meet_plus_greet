# Generated by Django 5.0.6 on 2024-06-03 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airport', '0002_alter_airport_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='terminal',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
