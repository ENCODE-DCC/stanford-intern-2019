# Generated by Django 2.2.2 on 2019-06-26 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s3_key', models.CharField(max_length=64, unique=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('experiment', models.CharField(max_length=64)),
                ('assay_title', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_name', models.CharField(db_index=True, max_length=32)),
                ('bucket', models.CharField(max_length=16, null=True)),
                ('time', models.DateTimeField(null=True)),
                ('ip_address', models.GenericIPAddressField(null=True)),
                ('requester', models.CharField(max_length=64, null=True)),
                ('request_id', models.CharField(max_length=16, unique=True)),
                ('operation', models.CharField(max_length=16, null=True)),
                ('s3_key', models.CharField(max_length=64, null=True)),
                ('request_uri', models.CharField(max_length=1024, null=True)),
                ('http_status', models.PositiveSmallIntegerField(null=True)),
                ('error_code', models.CharField(max_length=16, null=True)),
                ('bytes_sent', models.BigIntegerField(null=True)),
                ('object_size', models.BigIntegerField(null=True)),
                ('total_time', models.PositiveIntegerField(null=True)),
                ('turn_around_time', models.PositiveIntegerField(null=True)),
                ('referrer', models.URLField(null=True)),
                ('user_agent', models.CharField(max_length=128, null=True)),
                ('version_id', models.CharField(max_length=128, null=True)),
            ],
        ),
    ]
