# Generated by Django 5.0.4 on 2024-05-14 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aprovisionamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=255)),
                ('cedula', models.IntegerField()),
                ('nombre', models.CharField(max_length=255)),
                ('celula', models.CharField(max_length=255)),
                ('lider', models.CharField(max_length=255)),
            ],
        ),
    ]
