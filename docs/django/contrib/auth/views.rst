Представления
=============

login
-----

.. py:method:: django.contrib.auth.views.login()

    Страница авторизации пользователя

    .. code-block:: py

        # urls.py

        urlpatterns = patterns(
            '',

            # контекст по умолчанию form, next
            url(
                r'^login/',
                "django.contrib.auth.views.login",
                {
                    "template_name": "login.html",
                    "extra_context": {},
                },
                name="login",
            ),
        )

    .. code-block:: html

        <!-- login.html -->

        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Войти">
            <input type="hidden" name="next" value="{{ next }}">
        </form>


logout
------

.. py:method:: django.contrib.auth.views.logout()

    Страница выхода пользователя

    .. code-block:: py

        # urls.py

        urlpatterns = patterns(
            '',
            url(
                r'^logout/',
                "django.contrib.auth.views.logout",
                {            {
                    "template_name": "login.html",
                    "next_page": "",
                    "extra_context": {},
                },
                name="logout",
            ),
        )


logout_then_login
-----------------

.. py:method:: django.contrib.auth.views.logout()

    Страница выхода с редиректом на страницу авторизации

    .. code-block:: py

        # urls.py

        urlpatterns = patterns(
            '',
            url(
                r'^logout/',
                "django.contrib.auth.views.logout_then_login",
                {
                    "extra_context": {},
                },
                name="logout",
            ),
        )