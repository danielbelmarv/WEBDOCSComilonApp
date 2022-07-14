# Generated by Django 4.0.6 on 2022-07-14 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_alter_plato_miniatura'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('correo', models.CharField(max_length=60, null=True)),
                ('usuario', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='pedido',
            name='id_transaccion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='DireccionEnvio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=70)),
                ('ciudad', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=50)),
                ('codigo_postal', models.CharField(max_length=20)),
                ('fecha_agregado', models.DateField()),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.cliente')),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, default=0, null=True)),
                ('fecha_agregado', models.DateField()),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.pedido')),
                ('plato', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.plato')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.cliente'),
        ),
    ]