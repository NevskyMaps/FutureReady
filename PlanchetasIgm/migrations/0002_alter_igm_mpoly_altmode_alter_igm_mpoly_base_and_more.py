# Generated by Django 4.2.3 on 2023-09-01 15:27

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlanchetasIgm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='igm_mpoly',
            name='altmode',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='igm_mpoly',
            name='base',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='igm_mpoly',
            name='clamped',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='igm_mpoly',
            name='extruded',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='igm_mpoly',
            name='folderpath',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='igm_mpoly',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='igm_mpoly',
            name='name',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='igm_mpoly',
            name='popupinfo',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='igm_mpoly',
            name='shape_area',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='igm_mpoly',
            name='shape_leng',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='igm_mpoly',
            name='snippet',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='igm_mpoly',
            name='symbolid',
            field=models.BigIntegerField(null=True),
        ),
    ]
