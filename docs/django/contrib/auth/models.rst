Модели
======

.. code-block:: py

    from django.contrib.auth.models import User

User
----

.. py:class:: django.contrib.auth.models.User

    Пользователь

    .. py:attribute:: email

        Строка, электронная почта

    .. py:attribute:: is_active

        Булево, активный пользователь

    .. py:attribute:: is_staff

        Булево, персонал сайта, имеет возможность войти в админку

    .. py:attribute:: is_superuser

        Булево, суперпользователь

    .. py:method:: get_full_name()

        Возвращает строку, фамилию и имя пользователя

    .. py:method:: get_short_name()

        Возвращает строку, фамилию пользователя

    .. py:method:: get_username()

        Возвращает строку, логин пользователя

    .. py:method:: has_perm(perm_str)

        Возвращает булево, имеет ли пользователь указанное право

        .. code-block:: py

            def some_view(request):
                if request.user.is_authenticated():
                    if request.user.has_perm("good.add_good"):
                        ...

    .. py:method:: has_perms(perms_list)

        Возвращает булево, имеет ли пользователь указанные права

        .. code-block:: py

            def some_view(request):
                if request.user.is_authenticated():
                    if request.user.has_perms(
                        ["good.add_good", "good.delete_good"]):
                        ...

    .. py:method:: is_anonymous()

        Возвращает булево, гость

    .. py:method:: is_authenticated()

        Возвращает булево, авторизован ли пользователь.