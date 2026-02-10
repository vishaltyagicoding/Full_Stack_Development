from django.apps import AppConfig


class SignalEmailConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signal_email'

    def ready(self):
        import signal_email.signals
