from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from movies.models.categories import Category
from movies.serializers.categories import CategorySerializer, CategoryListSerializer


class CategoryView(GenericAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

    def get(self, request, pk, *args, **kwargs):
        category = Category.objects.filter(pk=pk)
        serializer = self.get_serializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryListByParent(GenericAPIView):
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        return Category.objects.all()

    def get(self, request, parent_id, *args, **kwargs):
        categories = Category.objects.filter(parent_id=parent_id)
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoriesListView(ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

    def get_queryset(self):
        return Category.objects.all()

    def get(self, request, *args, **kwargs):
        categories = Category.objects.filter(parent_id__isnull=True)
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

