# Generated by Django 3.2.9 on 2023-02-21 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomApp', '0115_auto_20230130_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bvrequest',
            name='request_id',
            field=models.CharField(default='Ti5YLbMc', max_length=20),
        ),
        migrations.AlterField(
            model_name='presignup',
            name='signup_token',
            field=models.CharField(default='IOmNDu1pmR', editable=False, max_length=255, unique=True),
        ),
    ]
