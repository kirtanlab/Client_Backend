# Generated by Django 3.2.9 on 2023-10-19 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hhi', '0051_auto_20231019_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bvrequest',
            name='request_id',
            field=models.CharField(default='7XqsAVoT', max_length=20),
        ),
        migrations.AlterField(
            model_name='presignup',
            name='signup_token',
            field=models.CharField(default='T4602kLT4Z', editable=False, max_length=255, unique=True),
        ),
    ]
