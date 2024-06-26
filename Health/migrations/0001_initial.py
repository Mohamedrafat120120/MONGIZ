# Generated by Django 5.0.3 on 2024-05-22 19:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='health_state',
            fields=[
                ('User', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Name', models.CharField(default=None, max_length=200)),
                ('Age', models.IntegerField()),
                ('Blood_Quarter', models.CharField(choices=[('A+', 'A Plus'), ('A-', 'A Minus'), ('B+', 'B Plus'), ('B-', 'B Minus'), ('AB+', 'Ab Plus'), ('AB-', 'Ab Minus'), ('O+', 'O Plus'), ('O-', 'O Minus')], default=None, max_length=3)),
                ('Health_Problem', models.TextField(blank=True, default=None, max_length=500, null=True)),
            ],
        ),
    ]
