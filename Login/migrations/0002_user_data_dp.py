# Generated by Django 3.0.4 on 2020-04-02 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='dp',
            field=models.ImageField(default='../dp.png', upload_to='DP'),
        ),
    ]
