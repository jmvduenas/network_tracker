# Generated by Django 2.2 on 2021-07-22 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ip_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='remarks',
            field=models.CharField(default=False, max_length=200, verbose_name='Comments'),
            preserve_default=False,
        ),
    ]
