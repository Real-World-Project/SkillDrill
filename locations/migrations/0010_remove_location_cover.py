# Generated by Django 2.2.12 on 2021-06-26 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0009_auto_20210626_0704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='cover',
        ),
    ]