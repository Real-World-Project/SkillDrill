# Generated by Django 2.2.12 on 2021-06-22 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0005_auto_20210622_0827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='image',
        ),
        migrations.AddField(
            model_name='location',
            name='cover',
            field=models.FileField(default='img/location/kathmandu.jpeg', upload_to='static/img/location'),
        ),
    ]