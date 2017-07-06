.. py:module:: http.client

http.client
===========

Модуль позволяет получить информацию из интернета по протоколу HTTP и HTTPS. 


HTTPConnection()
----------------

.. py:class:: HTTPConnection(<domen>[, port=80[, <strict>[, <timeout>[, [<source_address>]]]]])

    объект соединение

    * domen - домен, указывается без протокола
    * port - порт

    .. code-block:: py

        from http.client import HTTPConnection
        from urllib.parse import urlencode

        data = urlencode({'a': 'A'})
        headers = {
            'User-Agent': 'Mozila',
            'Accept': 'text/html',
            'Accept-Language': 'ru, ru-RU',
            'Accept-Charset': 'windows-1251',
            'Referer': '/'
        }

        con = HTTPConnection('ilnurgi1.ru')
        con.request('GET', '/home?%s' % data, headers=headers)
        result = con.getresponse()
        print(result.read().decode('cp1251'))
        con.close()

        headers = {
            'User-Agent': 'Mozila',
            'Accept': 'text/html',
            'Accept-Language': 'ru, ru-RU',
            'Accept-Charset': 'windows-1251',
            'Referer': '/',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        con = HTTPConnection('ilnurgi1.ru')
        con.request('POST', '/home', data, headers=headers)
        result = con.getresponse()
        print(result.read().decode('cp1251'))
        con.close()


    .. py:method:: close()

        закрывает объект соединения


    .. py:method:: getresponse()

        возвращает объект результата запроса :py:class:`HTTPResponse`


    .. py:method:: read([<количество байт>])

        Читает ответ севервера, без заголовков


    .. py:method:: request(method, path[, body=None][, headers])

        отправляет параметры запроса

        :param str method: метод запроса
        :param str path: путь от корня, для GET запроса данные также передаются тут
        :param str body: тело запроса для POST запроса
        :param dict headers: заголовки 


HTTPResponse()
--------------

.. py:class:: HTTPResponse()

    Ответ http запроса

    .. code-block:: py

        import urllib

        conn = urllib.request.open(url)


    .. py:attribute:: msg

        :py:class:`HTTPMessage` доп информация о заголовках ответа


    .. py:attribute:: reason

        строка, текстовый статус


    .. py:attribute:: status

        Число, код возврата запроса

        .. code-block:: py

            conn.status
            # 200


    .. py:attribute:: version

        число, версия протокола. (10 - HTTP/1.0, 11 - HTTP/1.1)


    .. py:method:: __next__()

        возвращает одну строку при каждом вызове, при достижении конца, будет возбуждено исключение :py:class:`StopIteration`


    .. py:method:: close()

        закрывает объект результата


    .. py:method:: getheader(<Заголовок>[, <Значение по умолчанию>=None])

        Возвращает значение указанного заголовка

        .. code-block:: py

            conn.getheader("Content-Type")
            # text/plain


    .. py:method:: getheaders()

        Возвращает все заголовки ответа сервера в виде списка кортежей

        .. code-block:: py

            conn.getheaders()
            # [("Content-Type", "text/plain"), ...]


    .. py:method:: geturl()

        возвращает урл адрес полученного документа


    .. py:method:: info()

        возвращает доп информацию в виде объекта :py:class:`HTTPMessage`


    .. py:method:: read([<количество байтов>])

        Возвращает строку, считанные данные

        .. code-block:: py

            data = conn.read()


    .. py:method:: readline([<количество байтов>])

        возвращает строку, считанные данные, считывает одну строку при каждом вызове


    .. py:method:: readlines([<количество байтов>])

        возвращает список, считанные данные, считывает одну строку при каждом вызове


HTTPMessage()
-------------

.. py:class:: HTTPMessage()

    доп информация результата запроса


    .. py:method:: as_string([unixform=Flase][, maxheaderlen=0])

        возвращает все заголовки ответа сервера в виде строки


    .. py:method:: get(<Заголовок>[, failobj=None])

        возвращает строку, значение указанного загловка


    .. py:method:: get_all(<Заголовок>[, failobj=None])

        возвращает список, значения указанного загловка


    .. py:method:: get_content_charset([failobj=None])

        возвращает кодировку из заголовка `Content-Type`


    .. py:method:: get_content_maintype()

        возвращает первую составляющую MIME-типа


    .. py:method:: get_content_subtype()

        возвращает вторую составляющую MIME_типа


    .. py:method:: get_content_type()

        возвращает MIME-тип документа из заголовка `Content-Type`


    .. py:method:: items()

        список всех заголовков ответа сервера


    .. py:method:: keys()

        список ключей в заголовках ответа сервера


    .. py:method:: values()

        список значений в заголовках ответа сервера