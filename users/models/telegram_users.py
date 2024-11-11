from django.db import models


class TelegramUser(models.Model):
    CHOICE_ROLE = (
        ('director', 'Director'),
        ('manager', 'Manager'),
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    first_name = models.CharField(max_length=100, verbose_name='First name')
    last_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Last name')
    username = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name='Username')
    role = models.CharField(max_length=15, default='user', choices=CHOICE_ROLE, null=True, blank=True, verbose_name='Role')
    premium = models.BooleanField(default=False, verbose_name='Premium')
    active = models.BooleanField(default=True, verbose_name='Active')
    telegram_id = models.PositiveBigIntegerField(unique=True, verbose_name='Telegram ID')

    class Meta:
        verbose_name = 'Telegram User'
        verbose_name_plural = 'Telegram Users'

    def __str__(self):
        return self.first_name
