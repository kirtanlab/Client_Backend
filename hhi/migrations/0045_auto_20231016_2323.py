# Generated by Django 3.2.9 on 2023-10-16 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hhi', '0044_auto_20231016_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bvrequest',
            name='request_id',
            field=models.CharField(default='0PpUERyc', max_length=20),
        ),
        migrations.AlterField(
            model_name='presignup',
            name='signup_token',
            field=models.CharField(default='27M8saZDiA', editable=False, max_length=255, unique=True),
        ),
    ]
