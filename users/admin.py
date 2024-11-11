from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from users.models.telegram_users import TelegramUser
from users.resources import TelegramUserResource


@admin.register(TelegramUser)
class TelegramUserAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'telegram_id')
    list_display_links = ('id',)
    list_filter = ('role', 'active')
    list_per_page = 10
    search_fields = ('first_name','username', 'telegram_id')
    resource_class = TelegramUserResource

