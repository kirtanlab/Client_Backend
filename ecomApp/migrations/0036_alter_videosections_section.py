# Generated by Django 3.2.9 on 2022-01-25 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomApp', '0035_alter_user_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videosections',
            name='section',
            field=models.CharField(choices=[('why_to_use', 'Why to use'), ('demo_videos', 'Demo Videos'), ('business_opportunity', 'Business Opportunity'), ('training_videos', 'Training Videos'), ('motivational_videos', 'Motivational Videos'), ('success_stories', 'Success Stories'), ('testimonial_videos', 'Testimonial Videos')], default=None, max_length=200, null=True),
        ),
    ]
