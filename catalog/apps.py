from django.apps import AppConfig


class CatalogAppConfig(AppConfig):
    name = 'catalog'
    verbose_name = 'Каталог'

    def ready(self):
        import catalog.signals
