# Generated by Django 2.2.3 on 2019-07-22 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_log_key_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='request_id',
            field=models.TextField(db_index=True, max_length=16),
        ),
    ]
