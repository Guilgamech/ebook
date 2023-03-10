# Generated by Django 3.2.13 on 2023-02-16 22:17

import ckeditor.fields
from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publishing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('date_update', models.DateField(auto_now=True, verbose_name='fecha de Modificacion')),
                ('date_delate', models.DateField(auto_now=True, verbose_name='fecha de Eliminacion')),
                ('name_publishing', models.CharField(max_length=100, unique=True, verbose_name='Nombre de la Editorial')),
                ('direction_publishing', models.CharField(max_length=255, verbose_name='Nombre de la Editorial')),
                ('phone_publishing', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Número de Teléfono de la Editorial')),
                ('email_publishing', models.EmailField(max_length=100, unique=True, verbose_name='Correo Electronico de la Editorial')),
                ('web_publishing', models.SlugField(max_length=255, unique=True, verbose_name='Web de la Editorial')),
                ('description_publishing', ckeditor.fields.RichTextField(verbose_name='Descripción de la Editorial')),
                ('counrty_publishing', django_countries.fields.CountryField(max_length=2, verbose_name='País de la Editorial')),
                ('city_publishing', models.CharField(max_length=100, verbose_name='Ciudad de la Editorial')),
                ('postal_code_publishing', models.PositiveIntegerField(verbose_name='Codigo Postal de la Editorial')),
                ('contact_publishing', models.CharField(max_length=100, unique=True, verbose_name='Contacto de la Editorial')),
                ('date_fundation_publishing', models.DateField(verbose_name='Fecha de Fundación de la Editorial')),
                ('image_publishing', models.ImageField(upload_to='editorial', verbose_name='Imagen de la Editorial')),
            ],
            options={
                'verbose_name': 'Publishing',
                'verbose_name_plural': 'Publishings',
            },
        ),
    ]
