# Generated by Django 2.2.12 on 2021-06-22 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_auto_20210622_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='image',
            field=models.ImageField(default='img/location/kathmandu.jpeg', upload_to='static/img/location'),
        ),
    ]
