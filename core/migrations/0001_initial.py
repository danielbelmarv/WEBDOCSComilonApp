# Generated by Django 4.0.4 on 2022-06-08 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_pedido', models.DateField()),
                ('estado_pedido', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Proovedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('esNuevo', models.BooleanField()),
                ('fecha_agregado', models.DateField()),
                ('miniatura', models.ImageField(upload_to='')),
                ('proovedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.proovedor')),
            ],
        ),
    ]