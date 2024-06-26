# Generated by Django 3.2.9 on 2022-06-03 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vestige', '0010_dailycheckin'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoinSection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('section_name', models.CharField(max_length=255)),
                ('ads_id', models.CharField(max_length=255)),
                ('reward_point', models.IntegerField()),
                ('minmax_point', models.CharField(max_length=18)),
                ('image', models.ImageField(blank=True, null=True, upload_to='CoinSection')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoinData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('section_type', models.CharField(max_length=255)),
                ('coin', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='VestigeCoinData', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
