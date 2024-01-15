# Generated by Django 4.0.3 on 2024-01-15 14:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='bus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.bus'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='date_created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='depart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='depart_location', to='api.location'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='destination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='api.location'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='fare',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='schedule',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'Active'), ('2', 'Cancelled')], default=1, max_length=2, null=True),
        ),
    ]