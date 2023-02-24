from django.db import models


class Base(models.Model):
    state = models.BooleanField('Estado', default=True)
    date_create = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)
    date_update = models.DateField('fecha de Modificacion', auto_now=True, auto_now_add=False)
    date_delate = models.DateField('fecha de Eliminacion', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
