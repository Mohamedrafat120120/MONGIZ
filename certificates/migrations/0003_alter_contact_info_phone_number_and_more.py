# Generated by Django 5.0.3 on 2024-05-22 23:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0002_contact_info_education_expereince_technical_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_info',
            name='Phone_Number',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='education',
            name='Graduation_Month_and_Year',
            field=models.DateField(default=datetime.date(2024, 5, 23), null=True),
        ),
        migrations.AlterField(
            model_name='expereince',
            name='Finish_Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='expereince',
            name='Start_Date',
            field=models.DateField(),
        ),
    ]
