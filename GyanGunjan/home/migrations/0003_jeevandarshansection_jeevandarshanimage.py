# Generated by Django 5.1.4 on 2025-01-21 11:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_landingpagesection_landingimage_delete_landingimages_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JeevanDarshanSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(help_text='Main title of the section', max_length=200)),
                ('section_description', models.TextField(help_text='Main description of the section')),
            ],
            options={
                'verbose_name': 'Jeevan Darshan Section',
                'verbose_name_plural': 'Jeevan Darshan Section',
            },
        ),
        migrations.CreateModel(
            name='JeevanDarshanImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='jeevan_darshan/')),
                ('image_title', models.CharField(help_text='Title for this image', max_length=200)),
                ('image_description', models.TextField(help_text='Description for this image')),
                ('section', models.ForeignKey(help_text='Associated Jeevan Darshan section', on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.jeevandarshansection')),
            ],
            options={
                'verbose_name': 'Jeevan Darshan Image',
                'verbose_name_plural': 'Jeevan Darshan Images',
            },
        ),
    ]