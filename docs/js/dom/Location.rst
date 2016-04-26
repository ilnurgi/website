Location - адрес текущей страницы
=================================

.. js:class:: Location()

    .. code-block:: js

        location;
        // http://ilnurgi.ru/info.aspx?id=10


    .. js:attribute:: hash

        Содержит якорную часть URL-адреса, включая начальный символ решетки (#)


    .. js:attribute:: host

        Часть URL-адреса, содержащая имя хоста и порт

        .. code-block:: js

            location.host;
            // ilnurgi.ru


    .. js:attribute:: hostname

        Часть URL-адреса, содержащая имя хоста


    .. js:attribute:: href

        Полный текст URL-адреса докумен­та


    .. js:attribute:: pathname

        Путь к запращиваемому страницы

        .. code-block:: js

            location.pathname;
            // /info.aspx


    .. js:attribute:: port

        Порт в  URL-ад­ре­се


    .. js:attribute:: protocol

        Протокол

        .. code-block:: js

            location.protocol;
            // http


    .. js:attribute:: search

        Строка запроса

        .. code-block:: js

            location.search;
            // ?id=10


    .. js:function:: assign(url)

        Загружает и отображает содержимое адреса `url`,
        как если бы значение `url` было присвоено свойству `href`.

        .. code-block:: js

            Location.assign(url);
            window.location.href = 'http://www.ilnurgi1.ru'
            window.location = 'http://www.ilnurgi1.ru'


    .. js:function:: reload([forceget])

        Повторно загружает текущий документ.

        * `forceget` - булево, true - загружать документ всегда из сети,
        иначе можно использовать кеш

        .. code-block:: js

            Location.reload();


    .. js:function:: replace(url)

        Загружает и отображает содержимое адреса `url`,
        замещая текущий документ в истории посещений,
        вследствие чего щелчок на кнопке `Back` броузера
        не вернет его к предыдущему документу.

        .. code-block:: js

            Location.replace('http://www.ilnurgi1.ru');


    .. js:function:: toString()

        Возвращает полный URL.

        .. code-block:: js

            location.toString();
            // http://www.ilnurgi1.ru
