# Generated by Django 3.0.7 on 2021-01-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20210114_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_4',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_5',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_6',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
