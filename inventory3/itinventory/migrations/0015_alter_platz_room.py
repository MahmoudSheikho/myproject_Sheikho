# Generated by Django 4.1.4 on 2022-12-20 14:22

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinventory', '0014_alter_platz_pc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platz',
            name='room',
            field=models.ForeignKey(default=None, null=True, on_delete=builtins.callable, related_name='Room', to='itinventory.rooms'),
        ),
    ]
