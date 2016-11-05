.. py:module:: urllib.request

urllib.request
==============


urlopen()
=========

.. py:method:: urlopen(<url-адрес или объект запроса>[, <POST-данные>][, <тайм-аут>][, cafile=None][, capath=None])

    выполняет запрос и возвращает результат ответа с сервера
    в виде объекта :py:class:`http.client.HTTPResponse`

    .. code-block:: py

        conn = urlopen(url)


Request()
=========

.. py:class:: Request(<url>[, data=None][, headers={}][, origin_req_host=None][, unverifiable=False])

    