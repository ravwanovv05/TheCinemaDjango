from django.db.models import Q
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import filters
from movies.models.movies import Movie
from movies.serializers.movies import MovieSerializer, FilterMovieSerializer
from datetime import datetime
import pytz


class MovieView(GenericAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()

    def get(self, request, pk, *args, **kwargs):
        movie = Movie.objects.filter(pk=pk)
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class MovieByCodeView(GenericAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()

    def get(self, request, code, *args, **kwargs):
        movie = self.get_queryset().filter(code=code).first()
        serializer = MovieSerializer(movie, many=False)
        return Response(serializer.data)


class MoviesListView(ListAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all().filter(invisible=False)

    def get_queryset(self):
        return Movie.objects.all()


class SearchMoviesView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)


class MoviFilterView(GenericAPIView):
    serializer_class = FilterMovieSerializer

    def get_queryset(self):
        return Movie.objects.all()

    def get(self, request, *args, **kwargs):
        timezone = pytz.timezone('Asia/Tashkent')
        current_year = datetime.now(timezone).year

        query = Q()
        from_year = int(request.data.get('from_year')) - 1 if request.data.get('from_year') else 1
        to_year = int(request.data.get('to_year')) + 1 if request.data.get('to_year') else current_year
        genre_id = request.data.get('genre_id')
        country_id = request.data.get('country_id')
        category_id = request.data.get('category_id')

        if from_year:
            from_year = int(from_year)
            query &= Q(year__gte=from_year)

        if to_year:
            to_year = int(to_year)
            query &= Q(year__lte=to_year)

        if genre_id:
            genre_id = int(genre_id)
            query &= Q(genre_id=genre_id)

        if country_id:
            country_id = int(country_id)
            query &= Q(country_id=country_id)

        if category_id:
            category_id = int(category_id)
            query &= Q(category_id=category_id)
        query &= Q(invisible=False)

        movies_list = Movie.objects.filter(query)
        serializer = MovieSerializer(movies_list, many=True)
        return Response(serializer.data)


class NewMoviesList(GenericAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()

    def get(self, request, *args, **kwargs):
        timezone = pytz.timezone('Asia/Tashkent')
        current_year = datetime.now(timezone).year
        movies_list = self.get_queryset().filter(Q(year__gt=current_year - 3 - 1) & Q(year__lt=current_year + 1))
        serializer = self.get_serializer(movies_list, many=True)
        return Response(serializer.data)
