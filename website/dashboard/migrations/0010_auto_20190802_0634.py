# Generated by Django 2.2.3 on 2019-08-02 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20190802_0255'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='log',
            name='dashboard_l_time_afed37_brin',
        ),
        migrations.AlterField(
            model_name='log',
            name='time',
            field=models.DateTimeField(db_index=True, null=True),
        ),
    ]
