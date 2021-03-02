# Generated by Django 3.1.7 on 2021-02-26 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('formulario', '0002_auto_20210226_1147'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Direccion',
        ),
        migrations.AddField(
            model_name='formulariobase',
            name='nacionalidad',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='formulariobase',
            name='texto1',
            field=models.TextField(blank=True, verbose_name='Poto1'),
        ),
        migrations.AddField(
            model_name='formulariobase',
            name='texto2',
            field=models.TextField(blank=True, verbose_name='Poto2'),
        ),
        migrations.AddField(
            model_name='formulariobase',
            name='texto3',
            field=models.TextField(blank=True, verbose_name='Poto3'),
        ),
        migrations.AddField(
            model_name='formulariobase',
            name='texto4',
            field=models.TextField(blank=True, verbose_name='Poto4'),
        ),
        migrations.AlterField(
            model_name='formulariobase',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='formulariobase',
            name='direccion',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='formulariobase',
            name='rut',
            field=models.CharField(default='', max_length=30),
        ),
    ]