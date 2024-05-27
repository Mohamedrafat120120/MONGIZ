# Generated by Django 5.0.3 on 2024-05-22 23:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medical_History', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicalhistory',
            fields=[
                ('User', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Name', models.CharField(default=None, max_length=50)),
                ('Age', models.IntegerField(default=None)),
                ('Chronic_Diseases', models.TextField(blank=True, default=None, max_length=255, null=True)),
                ('Another_Diseases', models.TextField(blank=True, default=None, max_length=255, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='medical_history',
        ),
    ]