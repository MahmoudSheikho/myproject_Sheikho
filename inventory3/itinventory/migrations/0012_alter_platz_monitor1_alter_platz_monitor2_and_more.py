# Generated by Django 4.1.4 on 2022-12-20 13:47

import builtins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itinventory', '0011_alter_platz_maus_alter_platz_monitor1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platz',
            name='monitor1',
            field=models.ForeignKey(default=1, null=True, on_delete=builtins.callable, related_name='Monitor1', to='itinventory.monitor'),
        ),
        migrations.AlterField(
            model_name='platz',
            name='monitor2',
            field=models.ForeignKey(default=1, null=True, on_delete=builtins.callable, related_name='Monitor2', to='itinventory.monitor'),
        ),
        migrations.AlterField(
            model_name='platz',
            name='pc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='itinventory.pcs'),
        ),
    ]
