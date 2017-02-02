android.widget.ListView
=======================

XML
---

.. code-block:: xml

    <ListView

        android:layout_width= "match_parent"
        android:layout_height= "wrap_content"

        android:id="@+id/lvMain" />


ListView
--------

.. py:class:: android.widget.ListView()

    Список

    .. code-block:: java

        ListView listView = (ListView) findViewById(R.id.listView);


    .. py:attribute:: CHOICE_MODE_SINGLE

        Константа, одиночный выбор элементов списка


    .. py:attribute:: CHOICE_MODE_MULTIPLE

        Константа, множественный выбор элементов списка


    .. py:method:: getCheckedItemPosition()

        Возвращает int, индекс выбранного элемента в списке

        .. code-block:: java

            int index = listView.getCheckedItemPosition();


    .. py:method:: getCheckedItemPositions()

        Возвращает :py:class:`android.util.SparseBooleanArray`,
        карта элементов списка, над которыми совершали действия

        .. code-block:: java

            SparseBooleanArray sbArray = listView.getCheckedItemPositions();


    .. py:method:: setAdapter(adapter)

        Устанавливает адаптер для списка

        .. code-block:: java

            ArrayAdapter<String> adapter = new ArrayAdapter<String>(
                context,
                android.R.layout.simple_list_item_1,
                names);

            listView.setAdapter(adapter);


    .. py:method:: setChoiceMode(mode)

        Устанавилвает режим выбора элементов списка

        .. code-block:: java

            listView.setChoiceMode(ListView.CHOICE_MODE_SINGLE);


    .. py:method:: setOnItemClickListener(listener)

        Обработчик клика по элементу

        * listener - :py:class:`android.widget.AdapterView.OnItemClickListener`


    .. py:method:: setOnItemSelectedListener(listener)

        Обработчик клика по элементу

        * listener - :py:class:`android.widget.AdapterView.OnItemSelectedListener`


    .. py:method:: setOnScrollListener(listener)

        Обработчик клика по элементу

        * listener - :py:class:`android.widget.AdapterView.OnItemClickListener`
