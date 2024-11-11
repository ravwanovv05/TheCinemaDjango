from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

from users.models.telegram_users import TelegramUser
from users.serializers.telegram_users import TelegramUserSerializer


class TelegramUserView(GenericAPIView):
    serializer_class = TelegramUserSerializer

    def get_queryset(self):
        return TelegramUser.objects.all()

    def get(self, request, telegram_id, *args, **kwargs):
        user = TelegramUser.objects.filter(telegram_id=telegram_id).first()
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TelegramUserListView(ListAPIView):
    serializer_class = TelegramUserSerializer
    queryset = TelegramUser.objects.all()

    def get_queryset(self):
        return TelegramUser.objects.all()


class TelegramUserUpdateView(GenericAPIView):
    serializer_class = TelegramUserSerializer

    def get_queryset(self):
        return TelegramUser.objects.all()

    def patch(self, request, user_id, *args, **kwargs):
        user = TelegramUser.objects.get(pk=user_id)
        serializer = self.get_serializer(user, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
