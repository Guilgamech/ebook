# Generated by Django 3.2.13 on 2023-02-16 22:17

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('date_update', models.DateField(auto_now=True, verbose_name='fecha de Modificacion')),
                ('date_delate', models.DateField(auto_now=True, verbose_name='fecha de Eliminacion')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Nombre del Libro')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripción del Libro')),
                ('image_front_page', models.ImageField(upload_to='libro', verbose_name='Imagen del Libro')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=8, null=True)),
                ('type_archive', models.FileField(help_text='Sube un PDF o un EPUB Archivo.', upload_to='archivos', validators=[django.core.validators.FileExtensionValidator(['pdf', 'epub'])], verbose_name='Archivos de los Libros ')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('date_update', models.DateField(auto_now=True, verbose_name='fecha de Modificacion')),
                ('date_delate', models.DateField(auto_now=True, verbose_name='fecha de Eliminacion')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Comentario')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('date_update', models.DateField(auto_now=True, verbose_name='fecha de Modificacion')),
                ('date_delate', models.DateField(auto_now=True, verbose_name='fecha de Eliminacion')),
                ('value', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='books.books')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
    ]
