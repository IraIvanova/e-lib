# Generated by Django 5.0.4 on 2024-05-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='cover',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='text',
            name='pages',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
