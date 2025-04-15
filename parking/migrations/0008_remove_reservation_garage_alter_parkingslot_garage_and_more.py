# Generated by Django 5.2 on 2025-04-15 16:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0007_reservation_garage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='garage',
        ),
        migrations.AlterField(
            model_name='parkingslot',
            name='garage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='parking.garage'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='parking_slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='parking.parkingslot'),
        ),
    ]
