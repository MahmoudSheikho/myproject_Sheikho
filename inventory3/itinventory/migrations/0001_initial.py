# Generated by Django 4.1.1 on 2022-09-21 08:33

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schnittstelle', models.CharField(max_length=255)),
                ('serialnummer', models.CharField(blank=True, default=None, max_length=55, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pcs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modell', models.CharField(max_length=255)),
                ('RAM', models.CharField(max_length=255)),
                ('CPU', models.CharField(max_length=255)),
                ('anzahlkerne', models.CharField(max_length=255)),
                ('festplatte', models.CharField(max_length=255, null=True)),
                ('pc', models.IntegerField(default=None, null=True)),
                ('serialnummer', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomname', models.CharField(max_length=255)),
                ('anzahlplaetze', models.IntegerField(default=None)),
                ('room', models.IntegerField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Platz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=50, null=True)),
                ('monitor1', models.ForeignKey(null=True, on_delete=builtins.callable, related_name='Monitor1', to='itinventory.monitor')),
                ('monitor2', models.ForeignKey(null=True, on_delete=builtins.callable, related_name='Monitor2', to='itinventory.monitor')),
                ('pc', models.ForeignKey(null=True, on_delete=builtins.callable, to='itinventory.pcs')),
                ('room', models.ForeignKey(default=None, null=True, on_delete=builtins.callable, to='itinventory.rooms')),
            ],
        ),
    ]
