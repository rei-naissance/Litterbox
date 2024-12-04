# Generated by Django 5.1.1 on 2024-12-04 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_rename_event_count_profile_like_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover_image',
            field=models.ImageField(blank=True, default='images/cover_photo.png', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='images/default_profile_pic.png', null=True, upload_to='images/'),
        ),
    ]
