# Generated by Django 3.2.9 on 2023-01-18 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vestige', '0029_auto_20230118_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='requiredcoinsforbill',
            name='min_items',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bvrequest',
            name='request_id',
            field=models.CharField(default='umICbPmg', max_length=20),
        ),
        migrations.AlterField(
            model_name='presignup',
            name='signup_token',
            field=models.CharField(default='pCLwlBlf2N', editable=False, max_length=255, unique=True),
        ),
    ]
