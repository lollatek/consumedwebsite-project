# Generated by Django 2.1.4 on 2019-01-13 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('press', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='press',
            name='press_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
