# Generated by Django 2.2.12 on 2021-07-08 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0025_auto_20210708_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='category',
        ),
        migrations.AddField(
            model_name='services',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='locations.Category'),
        ),
    ]