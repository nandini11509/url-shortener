# Generated by Django 4.2.6 on 2023-10-28 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urlshortener',
            old_name='short_url',
            new_name='short_code',
        ),
    ]
