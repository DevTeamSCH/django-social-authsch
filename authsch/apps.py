from django.conf import settings
from django.apps import AppConfig

settings.INSTALLED_APPS.append('social_django')


class AuthschConfig(AppConfig):
    name = 'authsch'
