# Generated by Django 2.2.2 on 2019-07-03 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20190702_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='object_size',
            field=models.BigIntegerField(db_index=True, null=True),
        ),
    ]
