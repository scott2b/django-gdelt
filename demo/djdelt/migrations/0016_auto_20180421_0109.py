# Generated by Django 2.0.4 on 2018-04-21 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djdelt', '0015_gkgmedia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gkgimage',
            name='document',
        ),
        migrations.RemoveField(
            model_name='socialimage',
            name='document',
        ),
        migrations.RemoveField(
            model_name='socialvideo',
            name='document',
        ),
        migrations.DeleteModel(
            name='GKGImage',
        ),
        migrations.DeleteModel(
            name='SocialImage',
        ),
        migrations.DeleteModel(
            name='SocialVideo',
        ),
    ]
