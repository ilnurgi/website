Сессии
======

Стандартная система аутентификации пользователей позволяет работать с сессиями.

Сессия каждого пользователя лежит в запросе и внешне представляет собой обычный словарь.


.. code-block:: py

    # settings.py

    INSTALLED_APPS += [
        'django.contrib.sessions.middleware.SessionMiddleware'
    ]


.. code-block:: py

    def some_view(request):

        session = request.session

