# Generated by Django 5.1.4 on 2025-01-09 06:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contribute'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandingPageData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LandingImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='landingImages/')),
                ('landing_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.landingpagedata')),
            ],
        ),
    ]