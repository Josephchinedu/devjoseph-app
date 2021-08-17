# Generated by Django 3.2.6 on 2021-08-17 18:11

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=300)),
                ('project_tag', models.CharField(max_length=100)),
                ('project_url', models.URLField()),
                ('project_published', models.BooleanField(default=True)),
                ('project_desc', models.TextField(blank=True, null=True)),
                ('project_lang', models.TextField(blank=True, null=True)),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
            ],
        ),
    ]
