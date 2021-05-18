# Generated by Django 2.2.19 on 2021-04-15 19:44

import aplic.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0002_auto_20210326_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='facebook',
            field=models.CharField(blank=True, max_length=200, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='professor',
            name='foto',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to=aplic.models.get_file_path, verbose_name='Foto'),
        ),
        migrations.AddField(
            model_name='professor',
            name='instagram',
            field=models.CharField(blank=True, max_length=200, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='professor',
            name='linkedin',
            field=models.CharField(blank=True, max_length=200, verbose_name='Linkedin'),
        ),
        migrations.AddField(
            model_name='professor',
            name='twitter',
            field=models.CharField(blank=True, max_length=200, verbose_name='Twitter'),
        ),
    ]
