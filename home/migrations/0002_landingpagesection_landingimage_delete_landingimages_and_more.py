# Generated by Django 5.1.4 on 2025-01-21 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandingPageSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_type', models.CharField(choices=[('hero1', 'Iks Gyan Gunjan'), ('hero2', '100 Regions'), ('hero3', 'Jeevan Darshan')], help_text='Select the section type (e.g., Iks Gyan Gunjan)', max_length=10, unique=True)),
                ('title', models.CharField(help_text='Main heading for the section', max_length=200)),
                ('short_description', models.TextField(help_text='Brief summary (1-2 sentences)')),
                ('long_description', models.TextField(help_text='Detailed description for the section')),
                ('additional_text', models.TextField(blank=True, help_text='Extra content (e.g., paragraph for Jeevan Darshan)')),
            ],
            options={
                'verbose_name': 'Landing Page Section',
                'verbose_name_plural': 'Landing Page Sections',
            },
        ),
        migrations.CreateModel(
            name='LandingImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Upload image for the section', upload_to='landing_images/')),
                ('caption', models.CharField(blank=True, help_text='Optional image caption', max_length=200)),
                ('section', models.ForeignKey(help_text='Select the section this image belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.landingpagesection')),
            ],
            options={
                'verbose_name': 'Section Image',
                'verbose_name_plural': 'Section Images',
            },
        ),
        migrations.DeleteModel(
            name='LandingImages',
        ),
        migrations.DeleteModel(
            name='LandingPageData',
        ),
    ]
