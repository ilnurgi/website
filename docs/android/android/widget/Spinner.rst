android.widget.Spinner
======================

XML
---

.. code-block:: xml

    <Spinner
        android:id="@+id/spinner"
        android:layout_width="match_parent"
        android:layout_height="wrap_content">
    </Spinner>


Spinner
-------

.. py:class:: android.widget.Spinner()

    Составной элемент, отображающий TextView
    в сочетании с соответствующим представлением ListView,
    которое позволяет выбрать элемент списка для отображения в текстовой строке.

    Сама строка состоит из объекта TextView, показывающего текущий выбор,
    и кнопки, при нажатии которой всплывает диалог выбора.

    Наследник :ref:`android.view.View`.

    .. code-block:: java

        Spinner spinner = (Spinner) findViewById(R.id.spinner);


    .. py:method:: getSelectedItem()


    .. py:method:: getSelectedItemPosition()

        Возвращает позицию выделенного элемента


    .. py:method:: setAdapter(ArrayAdapter adapter)

        Устанавливает адаптер


    .. py:method:: setOnItemSelectedListener(OnItemSelectedListener listener)

        Устанавливает слушателя выбора элемента

        * listener - :py:class:`android.widget.AdapterView.OnItemSelectedListener`


    .. py:method:: setPrompt(String prompt)

        Заголовок


    .. py:method:: setSelection(int pos)

        Выделяет элемент

