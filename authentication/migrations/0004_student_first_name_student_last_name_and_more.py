# Generated by Django 5.1.1 on 2024-10-02 03:03

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_student_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[authentication.models.validate_email]),
        ),
    ]
