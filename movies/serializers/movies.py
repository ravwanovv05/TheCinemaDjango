from rest_framework import serializers
from movies.models.categories import Category
from movies.models.movies import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        if (
                validated_data['category_id'].id == Category.objects.get(name='Serial').id
                and int(validated_data['part']) > 1
        ):
            invisible = True
        else:
            invisible = False

        return Movie.objects.create(
            title=validated_data['title'],
            year=validated_data['year'],
            part=validated_data['part'],
            code=validated_data['code'],
            invisible=invisible,
            genre_id=validated_data['genre_id'],
            country_id=validated_data['country_id'],
            language_id=validated_data['language_id'],
            category_id=validated_data['category_id'],
        )


class FilterMovieSerializer(serializers.ModelSerializer):
    from_year = serializers.IntegerField(write_only=True)
    to_year = serializers.IntegerField(write_only=True)

    class Meta:
        model = Movie
        fields = ('from_year', 'to_year', 'genre_id', 'country_id', 'category_id')


