# Generated by Django 5.0.4 on 2024-05-31 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0031_rename_fechainicio_contrato_abiertas_fechainiciocontrato'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cerradas',
            name='ANS_Días',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Ancho_Banda',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Asesor_Comercial',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Asignado_a',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Categoría_SM',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Causal_Finalizacion',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Causal_Retiro',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Ciudad_Instalacion',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Cuenta_Cliente',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Cumple_O_No_Cumple',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Direccion_Principal',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Fase_Actual',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Fecha_Creacion',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Fecha_Fin_Contrato',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Fecha_Finalizacion',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Fecha_Inicio_Contrato',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Grupo_Asignado',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Id_Aprovisionamiento',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Id_Servicio',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Medio_Ultima_Milla',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Modificado_por',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Nombre_Mes',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Nombre_Producto',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Observaciones_Finalizacion',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Proveedor_Ultima_Milla',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Sucursal_Instalcion',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Tiempo_Cliente',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Tiempo_Comercial',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Tiempo_ETB',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Tiempo_Operacion',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Tiempo_Real',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Tiempo_Tercero',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Tipo_Operacion_Plan',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Tipo_Solicitud',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Ultima_Anotación_Resumen',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Ultima_Fecha_Anotación',
        ),
        migrations.RemoveField(
            model_name='cerradas',
            name='Viabilidad_Origen',
        ),
        migrations.AddField(
            model_name='cerradas',
            name='ANSDías',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='AnchoBanda',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='AsesorComercial',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='Asignadoa',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='CategoríaSM',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='CausalFinalizacion',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='CausalRetiro',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='CiudadInstalacion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='CuentaCliente',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='CumpleNoCumple',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='DireccionPrincipal',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='FaseActual',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='FechaCreacion',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='FechaFinContrato',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='FechaFinalizacion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='FechaInicioContrato',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='GrupoAsignado',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='IdAprovisionamiento',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='IdServicio',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='MedioUltimaMilla',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='Modificadopor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='NombreMes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='NombreProducto',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='ObservacionesFinalizacion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='ProveedorUltimaMilla',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='SucursalInstalcion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='TiempoCliente',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='TiempoComercial',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='TiempoETB',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='TiempoOperacion',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='TiempoReal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='TiempoTercero',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='TipoOperacionPlan',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='TipoSolicitud',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='UltimaAnotación_Resumen',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='UltimaFechaAnotación',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cerradas',
            name='ViabilidadOrigen',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cerradas',
            name='Estado',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cerradas',
            name='NIT',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='cerradas',
            name='Segmento',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cerradas',
            name='TTAbierto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
