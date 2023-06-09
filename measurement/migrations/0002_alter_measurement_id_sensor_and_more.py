# Generated by Django 4.1.7 on 2023-03-17 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='id_sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensor', to='measurement.sensor'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
