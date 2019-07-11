# Generated by Django 2.2.3 on 2019-07-10 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_experimentlogpk'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(unique=True)),
                ('isp', models.CharField(max_length=64)),
                ('country', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='UniqueExperimentItemAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Log')),
            ],
        ),
        migrations.DeleteModel(
            name='ExperimentLogPk',
        ),
    ]