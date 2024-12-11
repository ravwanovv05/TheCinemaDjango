from django.db import models
from movies.models.categories import Category
from movies.models.countries import Country
from movies.models.genres import Genre
from movies.models.languages import Language


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    year = models.PositiveIntegerField(null=True, blank=True, verbose_name='Year')
    part = models.PositiveIntegerField(null=True, blank=True, verbose_name='Part')
    code = models.PositiveBigIntegerField(verbose_name='Code')
    invisible = models.BooleanField(default=False, verbose_name='Invisible')
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Genre ID')
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Country ID')
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name='Language ID')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category ID')

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.title
