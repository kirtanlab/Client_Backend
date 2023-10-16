# Generated by Django 3.2.9 on 2023-10-16 11:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('hhi', '0039_auto_20231016_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='hhiCreditTimer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('post_click_wvdo_btn', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pre_click_wvdo_btn', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='bvrequest',
            name='request_id',
            field=models.CharField(default='4YFb76cR', max_length=20),
        ),
        migrations.AlterField(
            model_name='presignup',
            name='signup_token',
            field=models.CharField(default='voUJcQQtsM', editable=False, max_length=255, unique=True),
        ),
    ]