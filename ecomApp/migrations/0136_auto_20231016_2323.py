# Generated by Django 3.2.9 on 2023-10-16 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomApp', '0135_auto_20231016_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bvrequest',
            name='request_id',
            field=models.CharField(default='tivCv0Lj', max_length=20),
        ),
        migrations.AlterField(
            model_name='presignup',
            name='signup_token',
            field=models.CharField(default='oYACAecqpl', editable=False, max_length=255, unique=True),
        ),
    ]
