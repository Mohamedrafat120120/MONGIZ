# Generated by Django 5.0.3 on 2024-04-23 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_national_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirm_password',
            field=models.CharField(default=None, max_length=200),
        ),
    ]