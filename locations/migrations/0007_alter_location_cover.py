# Generated by Django 3.2.4 on 2021-06-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0006_auto_20210622_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='cover',
            field=models.FileField(default='img/location/kathmandu.jpeg', upload_to='skilldrill/static/img/location'),
        ),
    ]