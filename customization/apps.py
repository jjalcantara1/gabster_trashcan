from django.apps import AppConfig


class CustomConfig(AppConfig):
    name = 'customization'

    def ready(self):
        import customization.signals