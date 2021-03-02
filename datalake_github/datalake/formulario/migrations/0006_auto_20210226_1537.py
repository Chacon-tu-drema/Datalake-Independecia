# Generated by Django 3.1.7 on 2021-02-26 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0005_auto_20210226_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulariobase',
            name='numero_casa',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='formulariobase',
            name='p_origen',
            field=models.CharField(default='', max_length=30, verbose_name='Pais de Origen'),
        ),
    ]
