# Generated by Django 4.2.3 on 2023-09-01 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PlanchetasIgm', '0002_alter_igm_mpoly_altmode_alter_igm_mpoly_base_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='igm_mpoly',
            name='altmode',
        ),
    ]