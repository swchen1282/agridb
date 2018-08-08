# Generated by Django 2.0.6 on 2018-08-08 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('household', '0002_auto_20180802_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandlordRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsidy', models.IntegerField(null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='household.Member')),
            ],
        ),
        migrations.CreateModel(
            name='LandlordRetire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsidy', models.IntegerField(null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='household.Member')),
            ],
        ),
        migrations.CreateModel(
            name='TenantList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='household.Member')),
            ],
        ),
        migrations.CreateModel(
            name='TenantTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsidy', models.IntegerField(null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='household.Member')),
            ],
        ),
    ]
