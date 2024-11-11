from import_export import resources
from movies.models.categories import Category
from movies.models.countries import Country
from movies.models.languages import Language
from movies.models.movies import Movie


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class MovieResource(resources.ModelResource):
    class Meta:
        model = Movie


class CountryResource(resources.ModelResource):
    class Meta:
        model = Country

class LanguageResource(resources.ModelResource):
    class Meta:
        model = Language
