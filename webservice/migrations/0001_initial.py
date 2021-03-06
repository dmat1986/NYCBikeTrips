# Generated by Django 2.2.24 on 2022-03-01 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ride_id', models.CharField(default='', max_length=20)),
                ('rideable_type', models.CharField(default='', max_length=50)),
                ('start_station_name', models.CharField(default='', max_length=100)),
                ('start_station_id', models.CharField(default='', max_length=10)),
                ('end_station_name', models.CharField(default='', max_length=100)),
                ('end_station_id', models.CharField(default='', max_length=10)),
                ('start_lat', models.CharField(default='', max_length=20)),
                ('start_lng', models.CharField(default='', max_length=20)),
                ('end_lat', models.CharField(default='', max_length=20)),
                ('end_lng', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.CharField(default='', max_length=20)),
                ('ended_at', models.CharField(default='', max_length=20)),
                ('conditions', models.CharField(default='', max_length=20)),
                ('temperature', models.CharField(default='', max_length=20)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webservice.Route')),
            ],
        ),
    ]
