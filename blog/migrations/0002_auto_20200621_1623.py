# Generated by Django 2.2.13 on 2020-06-21 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published_data',
            new_name='published_date',
        ),
    ]
