# Generated by Django 5.1.1 on 2024-10-30 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_comment_is_deleted_post_is_deleted_notification_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='report',
            unique_together=set(),
        ),
    ]
