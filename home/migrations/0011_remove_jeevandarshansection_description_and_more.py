# Generated by Django 5.1.4 on 2025-02-07 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_jeevandarshanimage_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jeevandarshansection',
            name='description',
        ),
        migrations.RemoveField(
            model_name='thematic',
            name='section_type',
        ),
        migrations.AddField(
            model_name='jeevandarshansection',
            name='left_description',
            field=models.TextField(default='left ', help_text='Left side description for the philosophy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jeevandarshansection',
            name='right_description',
            field=models.TextField(default='right', help_text='Right side description for the philosophy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jeevandarshansection',
            name='short_description',
            field=models.TextField(default='short', help_text='Short description for homepage display'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='JeevanDarshanPhilosophyInfo',
        ),
    ]
