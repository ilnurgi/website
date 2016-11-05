# coding: utf-8

import os

import djcelery
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tts0qt$9)n&vwgupdl6gqd8sm4v!&tf+m3p=r03f=qrt4c2uyn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    'gunicorn',
    'djcelery',
    'djkombu',

    'application',
    'metrics',
    'blog',
    'fileuploader',
    "resume",
    "cars",

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'application.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'application.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db', 'db.sqlite3'),
    }
}

DATABASE_MONGO = {
    'host': 'localhost',
    'port': '27017',
    'nginx_access_db_name': 'nginx_access',
    'cpu_average_db_name': 'cpu_average',
    'mem_average_db_name': 'mem_average',
    'disk_io_db_name': 'disk_io_average',
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOG_PATH = os.path.join(BASE_DIR, 'logs')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ENVIRON_BIN_PATH = ''

settings_json = os.path.join(BASE_DIR, 'settings.yaml')

GOOGLE_SITE_VERIFICATION = ""

if os.path.exists(settings_json):
    globals().update(yaml.load(open(settings_json)))

parse_nginx_acces_log_path = os.path.join(LOG_PATH, 'nginx_access_parse_logs')
if not os.path.exists(parse_nginx_acces_log_path):
    os.makedirs(parse_nginx_acces_log_path)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'parse_nginx_access': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(parse_nginx_acces_log_path, 'log.log')
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'level': 'ERROR',
            'handlers': ['mail_admins' if not DEBUG else 'console']
        },
        'parse_nginx_access': {
            'level': 'DEBUG',
            'handlers': ['parse_nginx_access']
        }
    }
}

if DEBUG and 'console' in LOGGING['handlers']:
    LOGGING['loggers']['parse_nginx_access']['handlers'].append('console')

djcelery.setup_loader()

CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
BROKER_BACKEND = "djkombu.transport.DatabaseTransport"

LOGIN_REDIRECT_URL = "resume:home_page"
LOGIN_URL = "login"
LOGOUT_URL = "logout"

EXCLUDE_USER_AGENTS = {
    'MJ12bot/v1.4.5',
    "Baiduspider/2.0",
    "Googlebot/2.1",
    "YandexBot/3.0",
    "bingbot/2.0",
    "AhrefsBot/5.1",
    "http://riddler.io/about",
    "SemrushBot/1.1",
    "archive.org_bot",
}
