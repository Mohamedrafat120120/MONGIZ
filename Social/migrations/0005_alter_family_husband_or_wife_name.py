# Generated by Django 5.0.3 on 2024-05-18 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Social', '0004_remove_family_name_remove_family_sons_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='Husband_or_Wife_Name',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
