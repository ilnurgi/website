Авторизация
===========

.. code-block:: py

    from django.contrib import auth

authenticate
------------

.. py:method:: django.contrib.auth.authenticate(username, password)

    Аутентификация пользователя

    .. code-block:: py

        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )


login
-----

.. py:method:: django.contrib.auth.login(request, user)

    Авторизация пользователя

    .. code-block:: py

        login(request, user)


login_required
--------------

.. py:method:: django.contrib.auth.decorators.login_required

    Декоратор проверки авторизации пользователя

    .. code-block:: py

        from django.contrib.auth.decorators import login_required

        @login_required
        def index(request):
            return render(request, 'index.html')