# Generated by Django 3.2.9 on 2022-06-03 05:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vestige', '0006_orderproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(choices=[('Why to use', 'Why to use'), ('Demo Videos', 'Demo Videos'), ('Business Opportunity', 'Business Opportunity'), ('Training Videos', 'Training Videos'), ('Motivational Videos', 'Motivational Videos'), ('Success Stories', 'Success Stories'), ('Testimonial Videos', 'Testimonial Videos'), ('About Modicare', 'About Modicare'), ('Become a Partner', 'Become a Partner'), ('Previous Events', 'Previous Events'), ('Upcoming Events', 'Upcoming Events'), ('Book Ticket', 'Book Ticket'), ('Broucher', 'Broucher'), ('Earning Model', 'Earning Model')], max_length=100, unique=True)),
                ('section_image', models.ImageField(blank=True, null=True, upload_to='SectionImages')),
                ('section_name', models.CharField(choices=[('Why Modicare', 'Why Modicare'), ('Learnings', 'Learnings'), ('Archivers', 'Archivers'), ('Events', 'Events')], default=None, max_length=50)),
                ('section_type', models.CharField(choices=[('video', 'Video'), ('static', 'Static')], default=None, max_length=50, null=True)),
                ('section_data', models.URLField(blank=True, max_length=300, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
