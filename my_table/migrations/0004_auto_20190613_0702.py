# Generated by Django 2.2.2 on 2019-06-13 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_table', '0003_my_table_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel_Plan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='my_table',
            name='plan_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_table.Travel_Plan'),
            preserve_default=False,
        ),
    ]
