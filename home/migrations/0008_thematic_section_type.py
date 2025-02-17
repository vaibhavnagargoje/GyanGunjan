# Generated by Django 5.1.4 on 2025-02-06 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_flipbook_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='thematic',
            name='section_type',
            field=models.CharField(choices=[('All', 'All'), ('Nature_and_Agriculture', 'Nature_and_Agriculture'), ('Families_Communities_and_Social_Structure', 'Families_Communities_and_Social_Structure'), ('Art_Heritage_Cultural_Richness', 'Art_Heritage_Cultural_Richness'), ('Economy_Society_Local_Administration', 'Economy_Society_Local_Administration'), ('Knowledge and Learning', 'Knowledge and Learning')], default='All', help_text='Select the Philosophy type for Themetic  (e.g., Iks Gyan Gunjan) ', max_length=200, unique=True),
        ),
    ]
