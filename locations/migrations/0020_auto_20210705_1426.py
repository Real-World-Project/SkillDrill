# Generated by Django 2.2.12 on 2021-07-05 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0019_auto_20210705_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='category',
        ),
        migrations.AddField(
            model_name='services',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.Category'),
        ),
    ]
