# Generated by Django 5.0.3 on 2024-05-08 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work_career',
            name='ID_number',
        ),
        migrations.RemoveField(
            model_name='work_career',
            name='Name',
        ),
    ]