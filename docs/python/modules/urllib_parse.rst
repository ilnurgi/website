.. py:module:: urllib.parse

urllib.parse
============

.. warning::

    данный модуль доступен на третьей ветки питона


.. py:method:: parse_qs(<строка запроса>, [, keep_blankvalues=False][, strict_parsing=False][, encoding='utf-8'][, errors='replace'])

    разбирает строку запроса и возвращает словарь с ключами, содержащими названия параметров, и списка значений.

    :param bool keep_blankvalues: если истина, то параметры, не имеющие значений внутри строки запроса, также будут добавлены в результат.
    :param bool strict_parsing: если истина, то при наличии ошибки возбуждается исключение `ValueError`
    :param str encoding: кодировка данных
    :param str errors: уровень обработки ошибок

    >>> s = "str=%D1%F2%F0%EE%EA"&E0&v=10&v=20&t="
    >>> parse qs(s, encoding="cp1251")
    {'str': ['Строка'], 'v': ['10', '20']}
    >>> parse_qs(s, keep_Ыank_va1ues=True, encoding="cp1251")
    {'t': ["], 'str': ['Строка'], 'v': ['10', '20'])


.. py:method:: parse_qsl(<строка запроса>, [, keep_blankvalues=False][, strict_parsing=False][, encoding='utf-8'][, errors='replace'])

    аналогична :py:meth:`parse_qs`, только возвращает список кортежей, разбирает строку запроса

    :param bool keep_blankvalues: если истина, то параметры, не имеющие значений внутри строки запроса, также будут добавлены в результат.
    :param bool strict_parsing: если истина, то при наличии ошибки возбуждается исключение `ValueError`
    :param str encoding: кодировка данных
    :param str errors: уровень обработки ошибок

    >>> s = "str=%D1%F2%FO%EE%EA%EO&v=10&v=20&t="
    >>> parse qsl(s, encoding="cpl251")
    [('str', 'Строка'), ('v', '10'), ('v', '20')]
    >>> parse_qsl(s, keep_blank_values=True, encoding="cp1251")
    [('str', 'Строка'), ('v', '10'), ('v', '20'), ('t', ")]


.. py:method:: quote(<строка>[, safe='/'][, encoding=None][, errors=None])
    
    заменяет все специальные симолы последовательностями `%nn`. Цифры, анг­лийские буквы и символы подчеркивания, точки и дефиса не кодируются. Пробелы преобразуются в последовательность %20.

    :param str safe: символы, которые преобразовывать нельзя

    >>> quote("Cтpoкa", encoding="cp1251")
    '%D1%F2%F0%EE%EA%E0'
    >>> quote("Cтpoкa", encoding="utf-8")
    '%D0%A1%D1%82%D1%80%D0%BE%D0%BA%D0%B0'


.. py:method:: quote_plus(<строка>[, safe='/'][, encoding=None][, errors=None])

    функция аналогична функции :py:meth:`quote`, но пробелы заменяются символом `+`, а символ `/` заменяется на `%2F`

    :param str safe: символы, которые преобразовывать нельзя


.. py:method:: quote_from_bytes(<последовательность байтов>[, safe='/'])

    функция аналогична функции :py:meth:`quote`, но в качестве первого параметра принимает последовательность байтов


.. py:method:: unquote(<строка>[, encoding='utf-8'][, errors='replace'])

    заменяет последовательность `%nn` на соответсвующие символы. символ `+` не заменяется ничем

.. py:method:: unquote_plus(<строка>[, encoding='utf-8'][, errors='replace'])

    заменяет последовательность `%nn` на соответсвующие символы. символ `+` заменяет пробелом


.. py:method:: urlencode(<объект> [, doseq=False][, safe=''][, encoding=None][, errors=None])

    преобразовывает отдельные составляющие в строку запроса

    :param объект: словарь или список кортежей (кортеж из 2х элементов)
    :param bool doseq: если истина, то можно указать последовательность из нескольких значений во втором параметре кортежа

    >>> urlencode({"str": "Строка 2", "var": 20}, encoding="cpl251")
    'var=20&str='Шl%F2•;FO%EE%EA%E0+2'
    >>> urlencode([("str", "Строка 2"), ("var", 20)], encodiпg="cp1251")
    'str=%D1%F2%FO%EE%EA%E0+2&var=20' 


.. py:method:: urljoin(<базовый урл>, <относитьльный или абсолютный урл>[, <разбор якоря>])

    преобразует относитльный урл в абсолютный

    >>> from urllib.parse import urljoin
    >>> urljoin(http://admin.ru/f1/f2/test.html', 'file.html')
    'http://admin.ru/fl/f2/file.html'
    >>> urljoin(http://admin.ru/f1/f2/test.html', 'f3/file.html')
    'http://admin.ru/fl/f2/f3/file.html'
    >>> urljoin(http://admin.ru/f1/f2/test.html', '/file.html')
    'http://admin.ru/file.html'
    >>> urljoin(http://admin.ru/f1/f2/test.html', './file.html')
    'http://admin.ru/fl/f2/file.html'
    >>> urljoin(http://admin.ru/f1/f2/test.html', '../file.html')
    'http://admin.ru/fl/file.html'


.. py:method:: urlparse(<url> [, <схема> [, <разбор_якоря>=False]])
    
    возвращает :py:class:`ParseResult` с результатом разбора адреса

    :param схема: название протокола, если протокла нет в составе адреса
    :param bool разбор_якоря: если лож, то якорь будетвходить в состав других атрибутов

    >>> urlparse('http://ilnurgi.ru:80/test.php;st?var=5#metka')
    ParseResult(scheme='http', netloc='ilnurgi.ru:80', path='/test.php', params='st', query='var=5', fragment='metka')


.. py:method:: urlsplit(<url> [, <схема> [, <разбор_якоря>=False]])

    возвращает :py:class:`SplitResult` с результатом разбора адреса

    >>> urlsplit('http://ilnurgi.ru:80/test.php;st?var=5#metka')
    SplitResult(scheme='http', netloc='ilnurgi.ru:80', path='/test.php', query='var=5', fragment='metka')
    

.. py:method:: urlunparse(<последовательность>)
    
    возвращает строку, адрес, собранную из отдельных значений

    >>> urlunparse(('http', 'ilnurgi.ru:80', '/test.php', '', 'var=5', 'metka'))
    'http://ilnurgi.ru:80/test.php?var=5#metka'


.. py:method:: urlunsplit(<последовательность>)
    
    возвращает строку, адрес, собранную из отдельных значений

    >>> urlunsplit(('http', 'ilnurgi.ru:80', '/test.php', '', 'var=5', 'metka'))
    'http://ilnurgi.ru:80/test.php?var=5#metka'



.. py:class:: ParseResult()

    результат парсинга адреса


    .. py:attribute:: scheme

        название протокола


    .. py:attribute:: netloc

        название домена вместе с номером порта


    .. py:attribute:: path

        путь


    .. py:attribute:: hostname

        название домена в нижнем регистре


    .. py:attribute:: port 

        номер порта


    .. py:attribute:: params

        параметры


    .. py:attribute:: query

        строка запроса


    .. py:attribute:: fragment

        якорь


    .. py:attribute:: username

        имя пользователя


    .. py:attribute:: password

        пароль


    .. py:method:: geturl()

        возвращает адрес


.. py:class:: SplitResult()

    результат парсинга адреса
