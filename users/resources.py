from import_export import resources
from users.models.telegram_users import TelegramUser


class TelegramUserResource(resources.ModelResource):
    class Meta:
        model = TelegramUser
