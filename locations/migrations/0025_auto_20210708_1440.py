# Generated by Django 2.2.12 on 2021-07-08 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0024_auto_20210706_0800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='category',
        ),
        migrations.AddField(
            model_name='services',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='categories', to='locations.Category'),
        ),
    ]
