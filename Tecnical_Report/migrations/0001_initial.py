# Generated by Django 5.0.3 on 2024-05-04 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Issue', models.TextField(default='Write your issue', max_length=255)),
            ],
        ),
    ]