# Generated by Django 2.0.4 on 2018-04-21 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djdelt', '0011_auto_20180421_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='gkgdocument',
            name='amounts',
            field=models.TextField(blank=True),
        ),
    ]
