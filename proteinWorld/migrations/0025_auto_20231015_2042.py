# Generated by Django 3.2.9 on 2023-10-15 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proteinWorld', '0024_auto_20231015_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bvrequest',
            name='request_id',
            field=models.CharField(default='QZ3bT169', max_length=20),
        ),
        migrations.AlterField(
            model_name='presignup',
            name='signup_token',
            field=models.CharField(default='h1c1x8g3oH', editable=False, max_length=255, unique=True),
        ),
    ]