# Generated by Django 3.0.7 on 2020-07-12 07:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
