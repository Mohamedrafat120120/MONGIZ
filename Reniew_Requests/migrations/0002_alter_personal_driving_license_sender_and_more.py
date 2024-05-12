# Generated by Django 5.0.3 on 2024-05-12 22:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reniew_Requests', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_driving_license',
            name='Sender',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sender_driving_license', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='personal_id_card',
            name='Receive_Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='personal_id_card',
            name='Sender',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sender_reniew_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
