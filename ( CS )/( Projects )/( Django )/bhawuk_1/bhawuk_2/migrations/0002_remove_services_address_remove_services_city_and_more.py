# Generated by Django 4.1 on 2022-08-20 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bhawuk_2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='address',
        ),
        migrations.RemoveField(
            model_name='services',
            name='city',
        ),
        migrations.RemoveField(
            model_name='services',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='services',
            name='client_name',
            field=models.CharField(default='Bhawuk', max_length=100),
        ),
        migrations.AddField(
            model_name='services',
            name='creation_date',
            field=models.DateField(default=datetime.date(2022, 8, 20)),
        ),
        migrations.AddField(
            model_name='services',
            name='particulars',
            field=models.CharField(default='Suchna', max_length=100),
        ),
        migrations.AddField(
            model_name='services',
            name='publish_date',
            field=models.DateField(default=datetime.date(2022, 8, 20)),
        ),
        migrations.AddField(
            model_name='services',
            name='publish_edition',
            field=models.CharField(default='Kota', max_length=100),
        ),
        migrations.AddField(
            model_name='services',
            name='publish_rate',
            field=models.CharField(default='340', max_length=100),
        ),
        migrations.AddField(
            model_name='services',
            name='publish_space_position',
            field=models.CharField(default='6*4', max_length=100),
        ),
        migrations.AddField(
            model_name='services',
            name='remarks',
            field=models.CharField(default='GST Applicable', max_length=100),
        ),
        migrations.AddField(
            model_name='services',
            name='serial_no',
            field=models.CharField(default='64523', max_length=6),
        ),
        migrations.AlterField(
            model_name='services',
            name='publication',
            field=models.CharField(default='DB', max_length=100),
        ),
    ]
