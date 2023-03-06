# Generated by Django 4.0.4 on 2023-03-06 03:57

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('app', '0002_alter_bookmark_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]