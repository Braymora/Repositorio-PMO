# Generated by Django 5.0.4 on 2024-06-12 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0057_rename_codigotipo_backlog_codigo_tipo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backlog',
            name='plusminus',
        ),
    ]
