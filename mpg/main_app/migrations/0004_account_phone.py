# Generated by Django 5.0.6 on 2024-06-04 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_account_first_name_account_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]