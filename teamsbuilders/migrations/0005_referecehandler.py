# Generated by Django 3.2.9 on 2022-07-14 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teamsbuilders', '0004_auto_20220621_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='RefereceHandler',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('reference_number', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('referred', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referred_user', to=settings.AUTH_USER_MODEL)),
                ('referrer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reference', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('referrer', 'referred')},
            },
        ),
    ]
