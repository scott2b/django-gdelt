# Generated by Django 2.0.4 on 2018-04-21 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GKGDocument',
            fields=[
                ('gkg_record_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('source_collection', models.IntegerField(choices=[(1, 'Web'), (2, 'Citation only'), (3, 'Core'), (4, 'DTIC'), (5, 'JSTOR'), (6, 'Non-textual')])),
                ('source_common_name', models.CharField(max_length=100)),
                ('document_identifier', models.CharField(max_length=1024)),
                ('v1counts', models.TextField(blank=True)),
                ('v2counts', models.TextField(blank=True)),
                ('v1themes', models.TextField(blank=True)),
                ('v2themes', models.TextField(blank=True)),
                ('v1locations', models.TextField(blank=True)),
                ('v2locations', models.TextField(blank=True)),
                ('v1persons', models.TextField(blank=True)),
                ('v2persons', models.TextField(blank=True)),
                ('v1organizations', models.TextField(blank=True)),
                ('v2organizations', models.TextField(blank=True)),
                ('tone', models.TextField(blank=True)),
                ('dates', models.TextField(blank=True)),
                ('gcam', models.TextField(blank=True)),
                ('sharing_image', models.URLField(blank=True)),
                ('quotations', models.TextField(blank=True)),
                ('all_names', models.TextField(blank=True)),
                ('amounts', models.TextField(blank=True)),
                ('translation_info', models.TextField(blank=True)),
                ('extras_xml', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='GKGMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('media_type', models.CharField(max_length=18)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djdelt.GKGDocument')),
            ],
        ),
        migrations.CreateModel(
            name='PatternCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('cat_type', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'pattern categories',
            },
        ),
        migrations.CreateModel(
            name='PatternTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=100)),
                ('score', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djdelt.PatternCategory')),
            ],
        ),
    ]
