# Generated by Django 5.1.4 on 2025-01-23 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_aboutproject_tag_aboutprojectimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='is_short_film',
            field=models.BooleanField(default=False, help_text='Check if this movie is a short film'),
        ),
    ]