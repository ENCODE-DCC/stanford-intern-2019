# Generated by Django 2.2.2 on 2019-07-02 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20190627_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='experiment',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
