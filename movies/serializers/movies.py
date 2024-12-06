from rest_framework import serializers
from movies.models.movies import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class FilterMovieSerializer(serializers.ModelSerializer):
    from_year = serializers.IntegerField(write_only=True)
    to_year = serializers.IntegerField(write_only=True)

    class Meta:
        model = Movie
        fields = ('from_year', 'to_year', 'genre_id', 'country_id', 'category_id')


