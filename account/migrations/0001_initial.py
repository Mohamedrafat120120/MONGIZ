# Generated by Django 5.0.3 on 2024-05-11 23:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('birth_dt', models.DateField(default=datetime.date.today)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('national_id', models.CharField(max_length=15, unique=True)),
                ('phone_number', models.CharField(max_length=11, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('register_time', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
