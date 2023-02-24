from django.core.validators import FileExtensionValidator, MaxValueValidator
from django.db import models
from ckeditor.fields import RichTextField

from apps.author.models import Author
from apps.base.models import Base
from apps.gender.models import Gender
from apps.publishing.models import Publishing
from apps.user.models import User


class Books(Base):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    gender = models.ManyToManyField(Gender)
    publishing = models.ForeignKey(Publishing, on_delete=models.CASCADE)
    title = models.CharField("Nombre del Libro", max_length=100, unique=True)
    description = RichTextField('Descripción del Libro')
    image_front_page = models.ImageField("Imagen del Libro", upload_to='libro')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0, blank=True, null=True)
    archive = models.FileField(upload_to='archivos',
                                    verbose_name='Archivos de los Libros ',
                                    help_text='Sube un PDF o un EPUB Archivo.',
                                    validators=[FileExtensionValidator(['pdf', 'epub'])])

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title


class Comment(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='comments')
    text = RichTextField('Comentario')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.user.username} en {self.book.title}'

class Rating(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='ratings')
    value = models.PositiveIntegerField(validators=[MaxValueValidator(10)])

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'

        def __str__(self):
            return f'{self.user.username} valoró {self.value} en {self.book.title}'
