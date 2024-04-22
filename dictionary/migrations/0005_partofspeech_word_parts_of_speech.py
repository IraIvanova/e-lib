# Generated by Django 5.0.4 on 2024-04-13 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0004_alter_translation_word'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartOfSpeech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='word',
            name='parts_of_speech',
            field=models.ManyToManyField(to='dictionary.partofspeech'),
        ),
    ]
