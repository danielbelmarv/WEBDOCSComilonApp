# Generated by Django 4.0.4 on 2022-06-18 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_proovedor_proveedor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plato',
            old_name='proovedor',
            new_name='proveedor',
        ),
        migrations.AlterField(
            model_name='plato',
            name='miniatura',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
