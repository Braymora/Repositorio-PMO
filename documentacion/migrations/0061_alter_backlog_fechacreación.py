# Generated by Django 5.0.4 on 2024-06-12 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0060_alter_backlog_primerdíames'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backlog',
            name='FechaCreación',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
