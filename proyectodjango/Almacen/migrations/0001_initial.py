# Generated by Django 3.0.3 on 2020-02-13 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('fechaProducto', models.CharField(max_length=254)),
                ('FechaCaducidad', models.CharField(max_length=254)),
                ('cantidadProducto', models.CharField(max_length=254)),
                ('VentasProcuto', models.CharField(max_length=254)),
            ],
        ),
    ]