from django.db import models
from movies.models.categories import Category
from movies.models.countries import Country
from movies.models.languages import Language


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(null=True, blank=True, verbose_name='Description')
    year = models.PositiveIntegerField(null=True, blank=True, verbose_name='Year')
    series = models.PositiveIntegerField(null=True, blank=True, verbose_name='Series')
    code = models.PositiveBigIntegerField(verbose_name='Code')
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Country ID')
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name='Language ID')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category ID')

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.title
