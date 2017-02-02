android.net.Uri
===============

.. py:class:: android.net.Uri

    .. py:method:: parse(String uri)

        Статический метод, который парсит строку и возвращает :py:class:`android.net.Uri`

        .. code-block:: java

            Uri uri = Uri.parse("http://developer.android.com/reference/android/net/Uri.html")
            Uri uri = Uri.parse("http://ilnurgi@developer.android.com:80/reference/android/net/Uri.html")


    .. py:method:: getAuthority()

        .. code-block:: java

            uri.getAuthority();
            // developer.android.com


    .. py:method:: getHost()

        .. code-block:: java

            uri.getHost();
            // developer.android.com


    .. py:method:: getLastPathSegment()

        .. code-block:: java

            uri.getLastPathSegment();
            // Uri.html


    .. py:method:: getPath()

        .. code-block:: java

            uri.getPath();
            // /reference/android/net/Uri.html


    .. py:method:: getPort()

        .. code-block:: java

            uri.getPort();
            // 80


    .. py:method:: getScheme()

        .. code-block:: java

            uri.getScheme();
            // http


    .. py:method:: getSchemeSpecificPart()

        .. code-block:: java

            uri.getSchemeSpecificPart();
            // //developer.android.com/reference/android/net/Uri.html


    .. py:method:: getUserInfo()

        .. code-block:: java

            uri.getSchemeSpecificPart();
            // ilnurgi


