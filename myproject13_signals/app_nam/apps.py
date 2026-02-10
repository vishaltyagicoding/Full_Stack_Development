from django.apps import AppConfig


class AppNamConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_nam'

    def ready(self):
        import app_nam.signals
