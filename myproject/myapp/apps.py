from django.apps import AppConfig


class BackendConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        """
        импортируем сигналы
        """
