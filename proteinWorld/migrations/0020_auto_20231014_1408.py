# Generated by Django 3.2.9 on 2023-10-14 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proteinWorld', '0019_auto_20231014_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bvrequest',
            name='request_id',
            field=models.CharField(default='ulqpFCvE', max_length=20),
        ),
        migrations.AlterField(
            model_name='presignup',
            name='signup_token',
            field=models.CharField(default='VMS1UtnCzG', editable=False, max_length=255, unique=True),
        ),
    ]
