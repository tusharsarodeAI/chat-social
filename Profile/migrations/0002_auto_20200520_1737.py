# Generated by Django 3.0.4 on 2020-05-20 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='friends',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='dp',
            field=models.ImageField(upload_to='Profile'),
        ),
    ]
