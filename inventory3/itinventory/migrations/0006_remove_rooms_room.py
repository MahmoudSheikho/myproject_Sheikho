# Generated by Django 4.1.1 on 2022-09-30 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itinventory', '0005_monitor_bemaerkung_pcs_bemaerkung'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms',
            name='room',
        ),
    ]
