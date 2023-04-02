# Generated by Django 4.0.3 on 2023-04-02 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('mass_value', models.CharField(blank=True, max_length=20, verbose_name='Mass base')),
                ('mass_exponent', models.CharField(blank=True, max_length=20, verbose_name='Mass exponent')),
                ('volume_value', models.CharField(blank=True, max_length=20, verbose_name='Volume base')),
                ('volume_exponent', models.CharField(blank=True, max_length=20, verbose_name='Volume exponent')),
                ('gravity_constant', models.FloatField(verbose_name='Gravity constant')),
                ('orbiting', models.CharField(blank=True, max_length=200, verbose_name='Orbiting')),
            ],
        ),
    ]