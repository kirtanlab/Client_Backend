# Generated by Django 3.2.9 on 2023-10-15 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hhi', '0032_auto_20231014_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bvrequest',
            name='request_id',
            field=models.CharField(default='C5wkVTck', max_length=20),
        ),
        migrations.AlterField(
            model_name='presignup',
            name='signup_token',
            field=models.CharField(default='sQOLf8Pa2V', editable=False, max_length=255, unique=True),
        ),
    ]