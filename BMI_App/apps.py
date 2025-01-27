from django.apps import AppConfig


class BmiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BMI_App'

    def ready(self):
        import BMI_App.signals