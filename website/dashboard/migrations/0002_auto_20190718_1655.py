# Generated by Django 2.2.3 on 2019-07-18 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='referrer',
            field=models.TextField(null=True),
        ),
    ]
