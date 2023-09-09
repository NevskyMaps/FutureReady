# Generated by Django 4.2.3 on 2023-09-01 15:06

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IGM_Mpoly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('folderpath', models.CharField(max_length=254)),
                ('symbolid', models.BigIntegerField()),
                ('altmode', models.IntegerField()),
                ('base', models.FloatField()),
                ('clamped', models.IntegerField()),
                ('extruded', models.IntegerField()),
                ('snippet', models.CharField(max_length=254)),
                ('popupinfo', models.CharField(max_length=254)),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]