# Generated by Django 5.0.4 on 2024-05-29 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0004_abiertas_abiertasretiros_cerradas_facturacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='backlog',
            name='Asesor_Comercial',
            field=models.CharField(default='default_value', max_length=255),
        ),
    ]
