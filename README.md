django-authsch
=====

Django Application for AuthSCH

Quick start
-----------

1. Add "authsch" to your INSTALLED_APPS setting like this::

    ````python
    INSTALLED_APPS = [
        ...
        'social_django',
        'authsch',
    ]
    ````

2. settings.py

    ````python
    SOCIAL_AUTH_URL_NAMESPACE = 'social'

    AUTHENTICATION_BACKENDS = [
        'authsch.authentication.AuthSCHOAuth2',
        'django.contrib.auth.backends.ModelBackend',
    ]

    SOCIAL_AUTH_AUTHSCH_KEY = "key"
    SOCIAL_AUTH_AUTHSCH_SECRET = "secret"
    SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
    LOGIN_URL = "login/authsch/"
    ````

3. Run `python manage.py migrate` to create the authsch models.
