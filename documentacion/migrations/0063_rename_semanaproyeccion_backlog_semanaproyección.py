# Generated by Django 5.0.4 on 2024-06-13 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0062_rename_valorprorrateadooperacion_backlog_valorprorrateadooperación'),
    ]

    operations = [
        migrations.RenameField(
            model_name='backlog',
            old_name='SemanaProyeccion',
            new_name='SemanaProyección',
        ),
    ]
