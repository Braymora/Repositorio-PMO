# Generated by Django 5.0.4 on 2024-06-06 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0048_alter_aprovisionamiento_celula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aprovisionamiento',
            name='Cedula',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
