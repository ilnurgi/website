android.widget.ArrayAdapter
===========================

.. py:class:: android.widget.ArrayAdapter(Context context, int textViewResourceId, t[] objects)

    Адаптер, который в качестве данных использует массив

    Наследник:

        * :py:class:`android.widget.BaseAdapter`


    .. py:method:: add()
    .. py:method:: clear()


    .. py:method:: createFromResource(Context context, int resourceId, int viewResourceId)

        Статический метод, создает адаптер из ресурсов

        .. code-block:: java

            ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(
                context,
                R.array.names,
                android.R.layout.simple_list_item_single_choice);


    .. py:method:: insert()
    .. py:method:: remove()
    .. py:method:: setDropDownViewResources(int layoutId)
    .. py:method:: sort()


