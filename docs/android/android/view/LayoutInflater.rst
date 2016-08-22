android.view.LayoutInflater
===========================

.. py:class:: android.view.LayoutInflater()

    Позваоляет создавать вью элементы из xml.

    .. py:method:: inflate(int resourceId, ViewGroup root, boolean attachToRoot)

        Возвращает :py:class:`android.view.View` элемент

        .. code-block:: java

            View view = layoutInflater.inflate(R.layout.textView, null, false);

