# Generated by Django 3.2.9 on 2023-10-16 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amulyaHerbal', '0036_auto_20231016_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bvrequest',
            name='request_id',
            field=models.CharField(default='NEgW65zI', max_length=20),
        ),
        migrations.AlterField(
            model_name='presignup',
            name='signup_token',
            field=models.CharField(default='lvGNhNc0VD', editable=False, max_length=255, unique=True),
        ),
    ]
