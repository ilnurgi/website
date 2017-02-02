.. py:module:: android.content

Intent
======

.. py:class:: Intent()

    .. code-block:: java

        Intent intent = new Intent(this, SomeClass.class);


    .. py:method:: getBooleanExtra(String key)

        Возвращает дополнительные параметры из интента

        .. code-block:: java

            intent.getBooleanExtra(EXTRA_KEY);


    .. py:method:: putExtra(String name, boolean value)

        Добавляет параметры в интент в виде ключа и значения

        .. code-block:: java

            intent.putExtra(EXTRA_KEY, value);