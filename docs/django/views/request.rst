Запросы
=======

HttpRequest
-----------

.. py:class:: django.http.HttpRequest()

    Объект запроса

    .. py:attribute:: GET

        Словарь get данных

        .. code-block:: py

            def index(request):

                good_id = request.GET['id']

    .. py:attribute:: POST

        Словарь post данных

        .. code-block:: py

            def index(request):

                good_id = request.POST['id']

    .. py:attribute:: REQUEST

        Словарь get и post данных

    .. py:attribute:: method

        Строка, метод запроса

    .. py:attribute:: path

        Строка, адрес текущей страницы без домена и параметров запроса

    .. py:method:: build_absolute_uri()

        Возвращает строку, абсолютный путь до указанного относительного

        .. code-block:: py

            post_url = request.build_absolute_uri(
                post.get_absolute_url())