# Generated by Django 5.1.1 on 2024-10-16 07:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=1000, null=True)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title', models.CharField(max_length=255, null=True)),
                ('post_count', models.IntegerField(default=0)),
                ('comment_count', models.IntegerField(default=0)),
                ('event_count', models.IntegerField(default=0)),
                ('social_links', models.JSONField(blank=True, default=dict)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
