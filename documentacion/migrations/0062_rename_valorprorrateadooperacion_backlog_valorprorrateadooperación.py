# Generated by Django 5.0.4 on 2024-06-12 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0061_alter_backlog_fechacreación'),
    ]

    operations = [
        migrations.RenameField(
            model_name='backlog',
            old_name='ValorProrrateadoOperacion',
            new_name='ValorProrrateadoOperación',
        ),
    ]
