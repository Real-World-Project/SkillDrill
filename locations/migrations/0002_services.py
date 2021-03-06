# Generated by Django 2.2.12 on 2021-06-22 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=200)),
                ('manager', models.CharField(max_length=100)),
                ('charge', models.IntegerField()),
                ('location', models.ManyToManyField(blank=True, related_name='services', to='locations.Location')),
            ],
        ),
    ]
