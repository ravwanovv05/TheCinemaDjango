from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from movies.models.movies import Movie
from movies.serializers.movies import MovieSerializer, MovieListSerializer


class MovieView(GenericAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()

    def get(self, request, pk, *args, **kwargs):
        movie = Movie.objects.filter(pk=pk)
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieByCodeView(GenericAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()

    def get(self, request, code, *args, **kwargs):
        movie = Movie.objects.filter(code=code)
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MoviesListView(ListAPIView):
    serializer_class = MovieListSerializer
    queryset = Movie.objects.all()

    def get_queryset(self):
        return Movie.objects.all()
