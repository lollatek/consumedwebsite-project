# Generated by Django 2.1.4 on 2019-01-12 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='support',
            name='support_embed',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='support',
            name='support_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
