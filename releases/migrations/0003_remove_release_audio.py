# Generated by Django 2.1.4 on 2019-01-12 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0002_auto_20190109_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='release',
            name='audio',
        ),
    ]
