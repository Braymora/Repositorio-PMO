# Generated by Django 5.0.4 on 2024-06-06 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0044_alter_backlog_fechapactadacliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aprovisionamiento',
            name='Celula',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
    ]
