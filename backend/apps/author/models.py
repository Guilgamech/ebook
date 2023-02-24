from django.db import models
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField


from apps.base.models import Base


class Author(Base):
    name_author = models.CharField("Nombre del Autor", max_length=50)
    last_name_author = models.CharField("Nombre del Autor", max_length=50)
    date_born_author = models.DateField("Fecha de Nacimiento del Autor")
    date_dead_author = models.DateField("Fecha de Fallecimiento del Autor")
    nationality_author = CountryField("Nacionalidad del Autor", blank_label="Seleccione una nacionalidad")
    biography_author = RichTextField("Bibliografía del Autor")
    image_author = models.ImageField("Imagen del Autor", upload_to='autor')

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name_author
