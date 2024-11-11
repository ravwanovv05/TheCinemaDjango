from mptt.models import MPTTModel, TreeForeignKey
from django.db import models


class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True, verbose_name='Name')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

