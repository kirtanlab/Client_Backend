# Generated by Django 3.2.9 on 2023-10-19 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomApp', '0140_auto_20231019_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bvrequest',
            name='request_id',
            field=models.CharField(default='TgYLyrY5', max_length=20),
        ),
        migrations.AlterField(
            model_name='presignup',
            name='signup_token',
            field=models.CharField(default='YnKjhDqJK1', editable=False, max_length=255, unique=True),
        ),
    ]