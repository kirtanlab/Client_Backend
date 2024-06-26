# Generated by Django 3.2.9 on 2022-08-14 08:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('teamsbuilders', '0006_userreferral'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserUpi',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('upi_id', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamsbuilders.teamsbuildersuser')),
            ],
        ),
        migrations.CreateModel(
            name='UserPaytmWallet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('paytm_wallet', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamsbuilders.teamsbuildersuser')),
            ],
        ),
        migrations.CreateModel(
            name='UserBankAccount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('account_number', models.IntegerField()),
                ('ifsc_code', models.CharField(max_length=30)),
                ('account_holder_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamsbuilders.teamsbuildersuser')),
            ],
        ),
        migrations.CreateModel(
            name='UserActivePaymentDetails',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bank_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teamsbuilders.userbankaccount')),
                ('paytm_wallet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teamsbuilders.userpaytmwallet')),
                ('upi_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teamsbuilders.userupi')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamsbuilders.teamsbuildersuser')),
            ],
        ),
    ]
