# Generated by Django 3.2.9 on 2022-01-19 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomApp', '0022_alter_distributionpoint_cityname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributionpoint',
            name='dpName',
            field=models.CharField(max_length=100),
        ),
    ]
