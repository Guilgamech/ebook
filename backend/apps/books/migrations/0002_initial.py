# Generated by Django 3.2.13 on 2023-02-16 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gender', '0001_initial'),
        ('author', '0001_initial'),
        ('publishing', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='books.books'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='books',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.author'),
        ),
        migrations.AddField(
            model_name='books',
            name='gender',
            field=models.ManyToManyField(to='gender.Gender'),
        ),
        migrations.AddField(
            model_name='books',
            name='publishing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publishing.publishing'),
        ),
    ]