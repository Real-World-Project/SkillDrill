# Generated by Django 3.2.4 on 2021-07-14 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0032_auto_20210714_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='cover',
            field=models.FileField(default='img/location/lalitpur.jpeg', upload_to='img/location'),
        ),
    ]
