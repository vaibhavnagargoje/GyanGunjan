# Generated by Django 5.1.4 on 2025-02-11 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_remove_jeevandarshansection_coffee_table_book_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='thematic',
            name='book_pdf',
            field=models.FileField(blank=True, null=True, upload_to='Thematic/'),
        ),
    ]
