# Generated by Django 4.1.7 on 2023-03-17 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_id_sensor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='image',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='id_sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurement', to='measurement.sensor'),
        ),
    ]