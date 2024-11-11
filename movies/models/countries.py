from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Name')

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name
