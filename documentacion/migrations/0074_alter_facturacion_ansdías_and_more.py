# Generated by Django 5.0.4 on 2024-06-13 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0073_alter_facturacion_fechacreación_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturacion',
            name='ANSDías',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='Adicional',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='AnchoBanda',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='AsesorComercial',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='Asignadoa',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='CategoríaSM',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='CausalRetiro',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='CiudadInstalación',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='CuentaCliente',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='CumpleNoCumple',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='DireccionPrincipal',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='Estado',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='FaseActual',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='GrupoAsignado',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='IdAprovisionamiento',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='IdServicio',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='MedioUltimaMilla',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='Modificadopor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='NIT',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='NombreMes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='NombreProducto',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='ProveedorUltimaMilla',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='Segmento',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='SucursalInstalcion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='TTAbierto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='TiempoCliente',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='TiempoComercial',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='TiempoETB',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='TiempoOperacion',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='TiempoReal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='TiempoTercero',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='TipoOperacionPlan',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='TipoSolicitud',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='UltimaActualizacion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='ViabilidadOrigen',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
