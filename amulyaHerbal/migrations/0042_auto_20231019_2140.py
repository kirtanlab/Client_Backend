# Generated by Django 3.2.9 on 2023-10-19 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amulyaHerbal', '0041_auto_20231019_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bvrequest',
            name='request_id',
            field=models.CharField(default='kbErsbVp', max_length=20),
        ),
        migrations.AlterField(
            model_name='presignup',
            name='signup_token',
            field=models.CharField(default='somE15iTLo', editable=False, max_length=255, unique=True),
        ),
    ]
