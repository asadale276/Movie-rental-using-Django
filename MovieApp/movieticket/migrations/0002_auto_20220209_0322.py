# Generated by Django 2.2 on 2022-02-08 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieticket', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='project_title',
            new_name='movie_title',
        ),
    ]
