# Generated by Django 3.2.9 on 2023-10-16 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hhi', '0043_auto_20231016_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bvrequest',
            name='request_id',
            field=models.CharField(default='FOUtsW2V', max_length=20),
        ),
        migrations.AlterField(
            model_name='presignup',
            name='signup_token',
            field=models.CharField(default='M3ufno7gdb', editable=False, max_length=255, unique=True),
        ),
    ]
