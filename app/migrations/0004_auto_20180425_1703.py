# Generated by Django 2.0.4 on 2018-04-25 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180425_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldmodel',
            name='range_end',
            field=models.IntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='fieldmodel',
            name='range_start',
            field=models.IntegerField(editable=False),
        ),
    ]