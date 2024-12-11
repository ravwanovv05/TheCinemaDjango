from django.urls import path
from movies.views.categories import CategoryView, CategoriesListView
from movies.views.countries import CountryView
from movies.views.genres import GenresListView
from movies.views.languages import LanguageView
from movies.views.movies import MovieView, MoviesListView, MovieByCodeView, SearchMoviesView, MoviFilterView, \
    NewMoviesList

urlpatterns = [
    path('create-category', CategoryView.as_view(), name='create_category'),
    path('category-details/<int:pk>', CategoryView.as_view(), name='category_details'),
    path('categories-list', CategoriesListView.as_view(), name='categories'),

    path('create-movie', MovieView.as_view(), name='create_movie'),
    path('movie-details/<int:pk>', MovieView.as_view(), name='movie_details'),
    path('movie-by-code/<int:code>', MovieByCodeView.as_view(), name='movie_by_code'),
    path('movies-list', MoviesListView.as_view(), name='movies_list'),
    path('search-movies', SearchMoviesView.as_view(), name='search_movies'),
    path('filter-movies', MoviFilterView.as_view(), name='movies_by_year'),
    path('new-movies', NewMoviesList.as_view(), name='new_movies'),

    path('countries-list', CountryView.as_view(), name='countries_list'),
    path('languages-list', LanguageView.as_view(), name='languages_list'),

    path('genres-list', GenresListView.as_view(), name='genres_list'),
]
