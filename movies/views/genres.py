from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from movies.models.genres import Genre
from movies.serializers.genres import GenreSerializer


class GenresListView(GenericAPIView):
    serializer_class = GenreSerializer

    def get_queryset(self):
        return Genre.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

