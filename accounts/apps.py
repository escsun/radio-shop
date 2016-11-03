from django.apps import AppConfig


class AccountsAppConfig(AppConfig):
    name = 'accounts'
    verbose_name = 'Пользователи и группы'

    def ready(self):
        import accounts.signals
