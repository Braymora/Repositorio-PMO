# Generated by Django 5.0.4 on 2024-05-29 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0016_alter_backlog_fechafacturacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backlog',
            name='FechaFinalizacion',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
