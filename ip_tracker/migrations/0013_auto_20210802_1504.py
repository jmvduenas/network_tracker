# Generated by Django 2.2 on 2021-08-02 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ip_tracker', '0012_auto_20210802_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='serial_number',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Serial Number'),
        ),
        migrations.AlterField(
            model_name='network',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='network',
            name='device',
            field=models.CharField(max_length=200, verbose_name='Device'),
        ),
    ]
