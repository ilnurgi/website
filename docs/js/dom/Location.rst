Location - адрес текущей страницы
=================================

.. js:class:: Location()

    .. code-block:: js

        location
        // http://ilnurgi.ru/info.aspx?id=10


    .. js:attribute:: hash

        Со­дер­жит якор­ную часть URL-ад­ре­са, вклю­чая на­чаль­ный сим­вол ре­шет­ки (#)


    .. js:attribute:: host

        Часть URL-ад­ре­са, со­дер­жа­щая имя хос­та и  порт

        .. code-block:: js

            location.host;
            // ilnurgi.ru


    .. js:attribute:: hostname

        Часть URL-ад­ре­са, со­дер­жа­щая имя хос­та


    .. js:attribute:: href

        Пол­ный текст URL-ад­ре­са до­ку­мен­та


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

        За­гру­жа­ет и  ото­бра­жа­ет со­дер­жи­мое ад­ре­са url, как ес­ли бы зна­че­ние url бы­ло при­свое­но свой­ст­ву href.


    .. js:function:: reload(false)

        По­втор­но за­гру­жа­ет те­ку­щий до­ку­мент.


    .. js:function:: replace(url)

        За­гру­жа­ет и ото­бра­жа­ет со­дер­жи­мое ад­ре­са url, за­ме­щая те­ку­щий до­ку­мент в ис­то­рии по­се­ще­ний, вслед­ст­вие че­го щел­чок на кноп­ке Back бро­узе­ра не вер­нет его к пре­ды­ду­ще­му до­ку­мен­ту.