# Generated by Django 5.0.4 on 2024-06-12 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0058_remove_backlog_plusminus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backlog',
            name='FechaEntregaCliente2',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
