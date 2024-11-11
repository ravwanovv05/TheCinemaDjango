from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Name')

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.name
