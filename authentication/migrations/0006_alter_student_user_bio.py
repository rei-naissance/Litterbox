# Generated by Django 5.1.1 on 2024-11-03 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_student_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='user_bio',
            field=models.TextField(blank=True, default='This user has nothing to say'),
        ),
    ]