# Generated by Django 3.2.13 on 2023-02-16 22:17

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('date_update', models.DateField(auto_now=True, verbose_name='fecha de Modificacion')),
                ('date_delate', models.DateField(auto_now=True, verbose_name='fecha de Eliminacion')),
                ('name_gender', models.CharField(max_length=100, unique=True, verbose_name='Nombre del Género')),
                ('description_gender', ckeditor.fields.RichTextField(verbose_name='Descripción del Género')),
                ('image_gender', models.ImageField(upload_to='genero', verbose_name='Imagen del Género')),
            ],
            options={
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Genders',
            },
        ),
    ]