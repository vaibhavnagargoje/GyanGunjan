# Generated by Django 5.1.4 on 2025-01-23 06:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_movie_is_landing_movie_movie_is_recommended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutproject',
            name='tag',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='AboutProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_project/images/')),
                ('alt_text', models.CharField(blank=True, max_length=200, null=True)),
                ('about_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.aboutproject')),
            ],
        ),
    ]