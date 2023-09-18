# Generated by Django 4.2.3 on 2023-09-16 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminarapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='thumbnails'),
        ),
    ]