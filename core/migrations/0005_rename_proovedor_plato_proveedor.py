# Generated by Django 4.0.4 on 2022-06-26 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_proveedor_plato_proovedor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plato',
            old_name='proovedor',
            new_name='proveedor',
        ),
    ]