# Generated by Django 3.2.9 on 2021-12-05 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomApp', '0010_order_distributionpoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='distributionpoint',
            name='cityName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='distributionpoint',
            name='emailAddress',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='distributionpoint',
            name='pincode',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='distributionpoint',
            name='state',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
