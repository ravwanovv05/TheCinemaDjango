from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from movies.models.languages import Language
from movies.serializers.languages import LanguageSerializer


class LanguageView(GenericAPIView):
    serializer_class = LanguageSerializer

    def get_queryset(self):
        return Language.objects.all()

    def get(self, request, *args, **kwargs):
        languages = self.get_queryset()
        serializer = self.get_serializer(languages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



