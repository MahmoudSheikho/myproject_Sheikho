# Generated by Django 4.1.4 on 2022-12-20 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinventory', '0012_alter_platz_monitor1_alter_platz_monitor2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platz',
            name='maus',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='platz',
            name='tastatur',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
