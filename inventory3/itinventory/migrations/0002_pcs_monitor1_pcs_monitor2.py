# Generated by Django 4.1.1 on 2022-09-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pcs',
            name='monitor1',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='pcs',
            name='monitor2',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
