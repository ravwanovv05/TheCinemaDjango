from django.urls import path
from users.views.telegram_users import TelegramUserView, TelegramUserListView, TelegramUserUpdateView

urlpatterns = [
    path('create-tg-user', TelegramUserView.as_view(), name='create_tg_user'),
    path('tg-user-details/<int:telegram_id>', TelegramUserView.as_view(), name='tg_user_details'),
    path('tg-users-list', TelegramUserListView.as_view(), name='tg_users_list'),
    path('update-tg-user/<int:user_id>', TelegramUserUpdateView.as_view(), name='update_tg_user'),
]
