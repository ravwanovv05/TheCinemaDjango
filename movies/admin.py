from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from movies.models.countries import Country
from movies.models.genres import Genre
from movies.models.languages import Language
from movies.models.movies import Category, Movie
from movies.resources import CategoryResource, MovieResource, CountryResource, LanguageResource, GenreResource


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id',)
    list_filter = ('name',)
    list_per_page = 10
    search_fields = ('name',)
    resource_class = CategoryResource


@admin.register(Movie)
class MovieAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'series', 'code', 'category_id')
    list_display_links = ('id',)
    list_filter = ('category_id',)
    list_per_page = 10
    search_fields = ('title',)
    resource_class = MovieResource


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    list_filter = ('name',)
    list_per_page = 10
    search_fields = ('name',)
    resource_class = CountryResource


@admin.register(Language)
class LanguageAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    list_filter = ('name',)
    list_per_page = 10
    search_fields = ('name',)
    resource_class = LanguageResource


@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    list_filter = ('name',)
    list_per_page = 10
    search_fields = ('name',)
    resource_class = GenreResource
