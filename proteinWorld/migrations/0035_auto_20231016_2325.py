# Generated by Django 3.2.9 on 2023-10-16 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proteinWorld', '0034_auto_20231016_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bvrequest',
            name='request_id',
            field=models.CharField(default='Ig6DNPgX', max_length=20),
        ),
        migrations.AlterField(
            model_name='presignup',
            name='signup_token',
            field=models.CharField(default='Uu032kwTYG', editable=False, max_length=255, unique=True),
        ),
    ]
