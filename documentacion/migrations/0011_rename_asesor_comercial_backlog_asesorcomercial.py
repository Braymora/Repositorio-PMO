# Generated by Django 5.0.4 on 2024-05-29 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0010_rename_tiempo_cliente_backlog_tiempocliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='backlog',
            old_name='Asesor_Comercial',
            new_name='AsesorComercial',
        ),
    ]
