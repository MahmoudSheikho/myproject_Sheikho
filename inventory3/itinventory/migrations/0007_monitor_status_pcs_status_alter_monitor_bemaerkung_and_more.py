# Generated by Django 4.1.1 on 2022-10-05 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinventory', '0006_remove_rooms_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='status',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pcs',
            name='status',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='bemaerkung',
            field=models.CharField(blank=True, default=None, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='pcs',
            name='bemaerkung',
            field=models.CharField(blank=True, default=None, max_length=300, null=True),
        ),
    ]
