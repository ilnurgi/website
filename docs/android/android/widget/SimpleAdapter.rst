android.widget.SimpleAdapter
============================


.. py:class:: android.widget.SimpleAdapter()

    Адаптер, который в качестве данных использует map объект

    Каждый объект является список атрибутов

    Наследник:

        * :py:class:`android.widget.BaseAdapter`

        * :py:class:`android.widget.SpinnerAdapter`

    .. code-block:: java

        SimpleAdapter simpleAdapter = new SimpleAdapter(
            context,

            // ArrayList<Map<String, Object>>
            data,

            // int
            R.layout.item,

            // String[]
            from,

            // int[]
            to);


    .. py:method:: notifyDataSetChanged()

        Уведомляет адаптер об изменении данных


    .. py:method:: setViewBinder(ViewBinder viewBinder)

        Добавляет новый объект, который сопоставляет данные с вьюхами

        * viewBinder - :py:class:`android.widget.SimpleAdapter.ViewBinder`


    .. py:method:: setViewImage(ImageView view, int value)

        Вставляет текст в текстовые вьюшки


    .. py:method:: setViewText(TextView view, String text)

        Вставляет текст в текстовые вьюшки


ViewBinder
----------


.. py:class:: android.widget.SimpleAdapter.ViewBinder()

    .. py:method:: setViewValue(View view, Object data, String textRepresentation)



