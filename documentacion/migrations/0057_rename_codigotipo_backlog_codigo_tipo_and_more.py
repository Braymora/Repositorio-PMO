# Generated by Django 5.0.4 on 2024-06-12 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0056_rename_ultimaanotacion_backlog_ultimaanotación'),
    ]

    operations = [
        migrations.RenameField(
            model_name='backlog',
            old_name='CODIGOTIPO',
            new_name='CODIGO_TIPO',
        ),
        migrations.RenameField(
            model_name='backlog',
            old_name='ESTADOGENERAL',
            new_name='ESTADO_GENERAL',
        ),
        migrations.RenameField(
            model_name='backlog',
            old_name='SUBCODIGOTIPO',
            new_name='SUB_CODIGO_TIPO',
        ),
    ]
