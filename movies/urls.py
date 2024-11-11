from django.urls import path
from movies.views.categories import CategoryView, CategoryListByParent, CategoriesListView
from movies.views.countries import CountryView
from movies.views.languages import LanguageView
from movies.views.movies import MovieView, MoviesListView, MovieByCodeView

urlpatterns = [
    path('create-category', CategoryView.as_view(), name='create_category'),
    path('category-details/<int:pk>', CategoryView.as_view(), name='category_details'),
    path('categories-by-parent/<int:parent_id>', CategoryListByParent.as_view(), name='categories_by_parent'),
    path('categories-list', CategoriesListView.as_view(), name='categories_list'),

    path('create-movie', MovieView.as_view(), name='create_movie'),
    path('movie-details/<int:pk>', MovieView.as_view(), name='movie_details'),
    path('movie-by-code/<int:code>', MovieByCodeView.as_view(), name='movie_by_code'),
    path('movies-list', MoviesListView.as_view(), name='movies_list'),

    path('countries-list', CountryView.as_view(), name='countries_list'),
    path('languages-list', LanguageView.as_view(), name='languages_list'),
]
