# Generated by Django 5.0.4 on 2024-04-13 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=50)),
            ],
        ),
    ]
