# Generated by Django 2.2.2 on 2019-06-14 02:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_table', '0005_travel_plan_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel_plan',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to=settings.AUTH_USER_MODEL),
        ),
    ]
