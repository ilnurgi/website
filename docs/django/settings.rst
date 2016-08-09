Конфигурирование проекта
========================


ALLOWED_HOSTS
-------------

На каких хостах доступно приложение.

Не учитывается при отладке.

.. code-block:: py

    ALLOWED_HOSTS = ['*']

.. code-block:: py

    ALLOWED_HOSTS = ['127.0.0.1']


DATABASES
---------

Словарь с конфигурациями баз данных

.. code-block:: py

    DATABASES = {
        '': {
            '': ''
        }
    }


DEBUG
-----

Включает или отключает режим отладки

.. code-block:: py

    DEBUG = True


EMAIL_BACKEND
-------------

Обработчик почтовых писем

.. code-block:: py

    # для отладки, почта вываливается в консоль
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


EMAIL_HOST
----------

SMTP сервер, по умолчанию localhost.

.. code-block:: py

    EMAIL_HOST = 'smtp.gmail.com'


EMAIL_PORT
----------

SMTP порт, по умолчанию 25.

.. code-block:: py

    EMAIL_PORT = 587


EMAIL_HOST_USER
---------------

Пользователь SMTP сервера.

.. code-block:: py

    EMAIL_HOST_USER = 'your_account@gmail.com'


EMAIL_HOST_PASSWORD
-------------------

Пароль пользователя SMTP сервера.

.. code-block:: py

    EMAIL_HOST_PASSWORD = 'your_password'


EMAIL_USE_TLS
-------------

Использовать TLS защищенное соединение.

.. code-block:: py

    EMAIL_USE_TLS = True


EMAIL_USE_SSL
-------------

Использовать неявное TLS защищенное соединение.

.. code-block:: py

    EMAIL_USE_SSL = True


INSTALLED_APPS
--------------

Список используемых приложений в проекте

.. code-block:: py

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]


LANGUAGE_CODE
-------------

Код языка, используемого в проекте

.. code-block:: py

    # http://www.i18nguy.com/unicode/language-identifiers.html
    LANGUAGE_CODE = 'en-us'
    LANGUAGE_CODE = 'en'


LANGUAGES
---------

Список поддерживаемых языков

.. code-block::

    LANGUAGES = (
        ('en', 'English'),
        ('es', 'Spanish'),
    )


LOCALE_PATHS
------------

Список директории, где искать переводы

.. code-block::

    LOCALE_PATHS = (
        os.path.join(BASE_DIR, 'locale'),
    )

MEDIA_ROOT
----------

Папка для хранения всех медиа файлов, загруженных пользователями

.. code-block:: py

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


MEDIA_URL
---------

Путь до папки с медии, для шаблонов

.. code-block:: py

    MEDIA_URL = '/media/'


MIDDLEWARE_CLASSES
------------------

Список мидлвар

.. code-block:: py

    MIDDLEWARE_CLASSES = [
        ...
    ]


ROOT_URLCONF
------------

Модуль корневого конфигуратора урла

.. code-block:: py

    ROOT_URLCONF = ''


USE_I18N
--------

Включить систему локализации

.. code-block::

    USE_I18N = True

USE_L10N
--------

Включить локализацию форматирования: даты, числа

.. code-block::

    USE_L10N = False


USE_TZ
------

Дата и время с тайм зоной

.. code-block::

    USE_TZ = True


TIME_ZONE
---------

Тайм зона по умолчанию

.. code-block::

    TIME_ZONE = 'Europe/Moscow'
