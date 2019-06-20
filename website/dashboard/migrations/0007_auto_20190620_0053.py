# Generated by Django 2.2.2 on 2019-06-20 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20190620_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='error_code',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='operation',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='request_id',
            field=models.CharField(db_index=True, max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='request_uri',
            field=models.CharField(max_length=4096, null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='s3_key',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
