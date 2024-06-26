# Generated by Django 3.2.9 on 2022-03-04 05:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ecomApp', '0050_auto_20220304_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrochureSections',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('brochure_name', models.CharField(max_length=255, null=True)),
                ('brochure_image', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
