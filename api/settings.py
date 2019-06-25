import os
import dj_database_url
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "h-ahf3-dayg71aepi4)1#4v)o4(!2hyv#3=w11abcf+0oiz=89"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost:3000", "127.0.0.1:3000","http://localhost:8100", "localhost:8100" ,
                 "https://q-sbs-conference.herokuapp.com", "q-sbs-conference.herokuapp.com",  '127.0.0.1'
 ]

INSTALLED_APPS = [
    "app",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'frontend',
    "rest_framework",
    "corsheaders",


]

AUTH_USER_MODEL = "app.Account"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = "api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "api.wsgi.application"

#  Database
#  https://docs.djangoproject.com/en/1.11/ref/settings/#databases
#

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        "TEST": {"NAME": "testdatabase"},
    }
}

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, './api/staticfiles', 'static-root')

STATIC_URL = "/static/"

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'staticfiles'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, './api/staticfiles', 'media-root')
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = "static/admin/"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("app.core.auth.JwtAuth",),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

CORS_ORIGIN_WHITELIST = ("localhost:3000", "127.0.0.1:3000",
                         "http://localhost:8100", "localhost:8100" ,
                         "https://q-sbs-conference.herokuapp.com",
                         "q-sbs-conference.herokuapp.com")

GRAPHENE = {"SCHEMA": "api.schema.schema"}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

