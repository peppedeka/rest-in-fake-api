# Generated by Django 2.0.4 on 2018-04-27 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20180427_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apimodel',
            name='obj',
        ),
    ]
