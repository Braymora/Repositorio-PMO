# Generated by Django 5.0.4 on 2024-06-07 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0052_rename_medioultima_milla_backlog_medioultimamilla'),
    ]

    operations = [
        migrations.RenameField(
            model_name='backlog',
            old_name='ProveedorUltima_Milla',
            new_name='ProveedorUltimaMilla',
        ),
    ]
