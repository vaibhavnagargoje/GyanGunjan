# Generated by Django 5.1.4 on 2025-02-03 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_rename_pdf_file_pdfdocument_file_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdfdocument',
            name='search_vector',
        ),
    ]
