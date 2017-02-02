.. _django_contrib_auth:

Пользователи, права, авторизация
================================

Права задаются в виде app_name.action_model и есть три права:

    * add - добавление

    * change - изменение

    * delete - удаление

но можно создать и свои :ref:`models_meta_permissions`.


По умолчанию, в контекст шаблонов добавляются переменные user и perms.

* user - пользователь

    .. code-block:: html

        {% if user.is_authenticated %}
            ...
        {% endif %}

* perms - права, которыми обладает пользователь

    .. code-block:: html

        {% if perms.good.add_good %}
            ...
        {% endif %}


.. toctree::
    :maxdepth: 1

    decorators
    models
    views


Конфигурирование
----------------

* :ref:`settings_login_redirect_url`
* :ref:`settings_login_url`
* :ref:`settings_logout_url`


authenticate
------------

.. py:method:: django.contrib.auth.authenticate(username, password)

    Аутентификация пользователя, если пользователя нет вернет None.

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