# Generated by Django 5.0.4 on 2024-05-31 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0036_rename_ans_dias_facturacion_ansdias_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturacion',
            name='FechaEntregaCliente',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='FechaFacturacion',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='FechaFinContrato',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='FechaInicioContrato',
            field=models.DateTimeField(blank=True, max_length=255, null=True),
        ),
    ]
