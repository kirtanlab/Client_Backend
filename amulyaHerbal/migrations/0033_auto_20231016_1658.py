# Generated by Django 3.2.9 on 2023-10-16 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amulyaHerbal', '0032_auto_20231016_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bvrequest',
            name='request_id',
            field=models.CharField(default='OFEkolni', max_length=20),
        ),
        migrations.AlterField(
            model_name='presignup',
            name='signup_token',
            field=models.CharField(default='eOulAFazpQ', editable=False, max_length=255, unique=True),
        ),
    ]
