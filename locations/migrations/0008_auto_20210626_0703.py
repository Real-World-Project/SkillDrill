# Generated by Django 2.2.12 on 2021-06-26 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0007_alter_location_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='cover',
            field=models.FileField(default='img/location/kathmandu.jpeg', upload_to='SkillDrill/skilldrill/static/img/location'),
        ),
    ]
