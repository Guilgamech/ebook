from django.db import models
from ckeditor.fields import RichTextField

from apps.base.models import Base


class Gender(Base):
    name_gender = models.CharField("Nombre del Género", max_length=100, unique=True)
    description_gender = RichTextField('Descripción del Género')
    image_gender = models.ImageField("Imagen del Género", upload_to='genero')

    class Meta:
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'

    def __str__(self):
        return self.name_gender
