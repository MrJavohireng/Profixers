# Generated by Django 4.2 on 2025-05-19 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_workdays_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='active_days',
            field=models.ManyToManyField(to='MainApp.workdays'),
        ),
        migrations.AddField(
            model_name='services',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
    ]
