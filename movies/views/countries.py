from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from movies.models.countries import Country
from movies.serializers.countries import CountrySerializer


class CountryView(GenericAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        return Country.objects.all()

    def get(self, request, *args, **kwargs):
        countries = self.get_queryset()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
