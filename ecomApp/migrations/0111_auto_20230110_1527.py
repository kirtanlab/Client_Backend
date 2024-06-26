# Generated by Django 3.2.9 on 2023-01-10 09:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ecomApp', '0110_auto_20230109_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreSignUP',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('mob', models.CharField(editable=False, max_length=15)),
                ('signup_token', models.CharField(default='zb6lvVyFbg', editable=False, max_length=255, unique=True)),
                ('signup_data', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='bvrequest',
            name='request_id',
            field=models.CharField(default='9141sRQI', max_length=20),
        ),
    ]
