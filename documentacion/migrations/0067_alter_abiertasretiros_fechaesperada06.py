# Generated by Django 5.0.4 on 2024-06-13 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0066_alter_abiertasretiros_fechacreación'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abiertasretiros',
            name='FechaEsperada06',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
