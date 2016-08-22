android.content.Intent
======================

.. py:class:: android.content.Intent()
.. py:class:: android.content.Intent(Intent intent)
.. py:class:: android.content.Intent(String action)
.. py:class:: android.content.Intent(String action, Uri uri)
.. py:class:: android.content.Intent(String action, Uri uri, Context context, Class cls)
.. py:class:: android.content.Intent(Context context, Class cls)

    .. code-block:: java

        Intent intent = new Intent(this, SomeClass.class);
        Intent intent2 = new Intent("ru.ilnurgi1.intent.action.some_action");


    .. py:attribute:: ACTION_VIEW

        Константа для просмотра чего либо, в зависимости от данных

        .. code-block:: java

            Intent intent = new Intent(
                Intent.ACTION_VIEW,
                Uri.parse("http://developer.android.com"));

            Intent intent = new Intent(
                Intent.ACTION_VIEW,
                Uri.parse("http://developer.android.com"));

            Intent intent = new Intent(
                Intent.ACTION_VIEW,
                Uri.parse("http://developer.android.com"));


    .. py:method:: getAction()

        Возвращает String, название действия

        .. code-block:: java

            String action = intent.getAction()


    .. py:method:: getBooleanExtra(String key)

        Возвращает дополнительные параметры из интента

        .. code-block:: java

            intent.getBooleanExtra(EXTRA_KEY);


    .. py:method:: getStringExtra(String key)

        Возвращает дополнительные параметры из интента

        .. code-block:: java

            intent.getStringExtra(EXTRA_KEY);


    .. py:method:: putExtra(String name, value)
    .. py:method:: putExtra(Bundle extras)
    .. py:method:: putExtra(Intent intent)

        Добавляет параметры в интент в виде ключа и значения

        * name - String
        * extras - :py:class:`android.os.Bundle`
        * intent - :py:class:`android.content.Intent`
        * value
            * :py:class:`android.os.Bundle`
            * :py:class:`android.os.Parcelable`, :py:class:`android.os.Parcelable`[]
            * :py:class:`java.io.Serializable`
            * :py:class:`java.lang.CharSequence`, :py:class:`java.lang.CharSequence`[]
            * boolean, boolean[]
            * byte, byte[]
            * char, char[]
            * double, double[]
            * float, float[]
            * int, int[]
            * long, long[]
            * short, short[]
            * String, String[]

        .. code-block:: java

            intent.putExtra(EXTRA_KEY, value);

    .. py:method:: setAction(action)

        .. code-block:: java

            intent.setAction(Intent.ACTION_VIEW);


    .. py:method:: setData(Uri data)

        * data - :py:class:`android.net.Uri`

        .. code-block:: java

            intent.setData(Uri.parse("tel:12345"));