# Generated by Django 5.1.4 on 2025-02-03 08:50

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pdfdocument',
            old_name='pdf_file',
            new_name='file',
        ),
        migrations.AddField(
            model_name='pdfdocument',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.DeleteModel(
            name='SearchIndex',
        ),
    ]
