# Generated by Django 3.1.7 on 2021-03-10 04:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('formulario', '0010_auto_20210309_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulariobase',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
