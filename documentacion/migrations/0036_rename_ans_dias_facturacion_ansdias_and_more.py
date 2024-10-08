# Generated by Django 5.0.4 on 2024-05-31 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0035_alter_cerradas_nit_alter_cerradas_ttabierto_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facturacion',
            old_name='ANS_dias',
            new_name='ANSdias',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Ancho_Banda',
            new_name='AnchoBanda',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Asesor_Comercial',
            new_name='AsesorComercial',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Asignado_a',
            new_name='Asignadoa',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Categoría_SM',
            new_name='CategoríaSM',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Causal_Retiro',
            new_name='CausalRetiro',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Ciudad_Instalacion',
            new_name='CiudadInstalacion',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Cuenta_Cliente',
            new_name='CuentaCliente',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Cumple_O_No_Cumple',
            new_name='CumpleNoCumple',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Direccion_Principal',
            new_name='DireccionPrincipal',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Fase_Actual',
            new_name='FaseActual',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Fecha_Creacion',
            new_name='FechaCreacion',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Fecha_Entrega_Cliente',
            new_name='FechaEntregaCliente',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Fecha_Facturacion',
            new_name='FechaFacturacion',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Fecha_Fin_Contrato',
            new_name='FechaFinContrato',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Fecha_Inicio_Contrato',
            new_name='FechaInicioContrato',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Grupo_Asignado',
            new_name='GrupoAsignado',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Id_Servicio',
            new_name='IdAprovisionamiento',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Medio_Ultima_Milla',
            new_name='IdServicio',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Modificado_por',
            new_name='MedioUltimaMilla',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Nombre_Mes',
            new_name='Modificadopor',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Nombre_Producto',
            new_name='NombreMes',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Proveedor_Ultima_Milla',
            new_name='NombreProducto',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Sucursal_Instalcion',
            new_name='ProveedorUltimaMilla',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Tiempo_Comercial',
            new_name='SucursalInstalcion',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Tiempo_Cliente',
            new_name='TiempoCliente',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Tipo_Operacion_Plan',
            new_name='TiempoComercial',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Tiempo_ETB',
            new_name='TiempoETB',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Tiempo_Operacion',
            new_name='TiempoOperacion',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Tiempo_Real',
            new_name='TiempoReal',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Tiempo_Tercero',
            new_name='TiempoTercero',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Tipo_Solicitud',
            new_name='TipoOperacionPlan',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Ultima_Actualizacion',
            new_name='TipoSolicitud',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='Viabilidad_Origen',
            new_name='UltimaActualizacion',
        ),
        migrations.RenameField(
            model_name='facturacion',
            old_name='id_Aprovisionamiento',
            new_name='ViabilidadOrigen',
        ),
    ]
