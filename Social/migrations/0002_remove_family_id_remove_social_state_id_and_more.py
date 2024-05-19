# Generated by Django 5.0.3 on 2024-05-18 21:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Social', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='family',
            name='id',
        ),
        migrations.RemoveField(
            model_name='social_state',
            name='id',
        ),
        migrations.AlterField(
            model_name='family',
            name='User',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='social_state',
            name='Marital_state',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], default='Single', max_length=10),
        ),
        migrations.AlterField(
            model_name='social_state',
            name='Personel_Card',
            field=models.ImageField(upload_to='social_state/Personel_Card/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='social_state',
            name='Phone_Number',
            field=models.CharField(default=None, max_length=11),
        ),
        migrations.AlterField(
            model_name='social_state',
            name='User',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
