# Generated by Django 2.2.2 on 2019-06-07 10:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_table', '0002_auto_20190607_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_table',
            name='note',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]