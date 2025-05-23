# Generated by Django 4.2 on 2025-05-10 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField()),
                ('phone_number', models.CharField(max_length=100)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MainApp.offer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MainApp.profile')),
            ],
        ),
        migrations.AddField(
            model_name='offer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MainApp.profile'),
        ),
    ]
