# Generated by Django 2.2.12 on 2021-08-17 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0035_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
