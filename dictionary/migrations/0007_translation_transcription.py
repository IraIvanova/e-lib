# Generated by Django 5.0.4 on 2024-05-11 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0006_alter_word_synonyms'),
    ]

    operations = [
        migrations.AddField(
            model_name='translation',
            name='transcription',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]