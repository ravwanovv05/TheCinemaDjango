# Generated by Django 4.2.1 on 2024-12-11 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='series',
            new_name='part',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='description',
        ),
    ]