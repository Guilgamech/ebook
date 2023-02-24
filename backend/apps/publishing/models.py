from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField


from apps.base.models import Base


class Publishing(Base):
    name_publishing = models.CharField("Nombre de la Editorial", max_length=100, unique=True)
    direction_publishing = models.CharField("Nombre de la Editorial", max_length=255, null=False)
    phone_publishing = PhoneNumberField('Número de Teléfono de la Editorial', unique=True, null=False)
    email_publishing = models.EmailField('Correo Electronico de la Editorial', unique=True, max_length=100)
    web_publishing = models.SlugField('Web de la Editorial', max_length=255, unique=True)
    description_publishing = RichTextField("Descripción de la Editorial")
    counrty_publishing = CountryField('País de la Editorial', blank_label="Seleccione el País")
    city_publishing = models.CharField('Ciudad de la Editorial', max_length=100)
    postal_code_publishing = models.PositiveIntegerField('Codigo Postal de la Editorial')
    contact_publishing = models.CharField('Contacto de la Editorial', max_length=100, unique=True)
    date_fundation_publishing = models.DateField('Fecha de Fundación de la Editorial')
    image_publishing = models.ImageField("Imagen de la Editorial", upload_to='editorial')

    class Meta:
        verbose_name = 'Publishing'
        verbose_name_plural = 'Publishings'

    def __str__(self):
        return self.name_publishing
