# Generated by Django 3.2.9 on 2022-08-15 03:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('teamsbuilders', '0009_userbankaccount_bank_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageVideos',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('sub_title', models.CharField(max_length=255)),
                ('video_link', models.URLField(blank=True, null=True)),
                ('embedded_url', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
