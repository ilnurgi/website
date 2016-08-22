android.widget.ExpandableListView
=================================


XML
---

.. code-block:: xml

    <ExpandableListView

        android:layout_width="match_parent"
        android:layout_height="wrap_content"

        android:id= "@+id/elvMain" />


ExpandableListView
------------------

.. py:class:: android.widget.ExpandableListView()

    .. code-block:: java

        expListView = (ExpandableListView) findViewById(R.id.expListView);


    .. py:method:: expandGroup(int groupPosition)

        Разворачивает группу

        .. code-block:: java

            expListView.expandGroup(2);


    .. py:method:: setAdapter(SimpleExpandableListAdapter adapter)

        Устанавливает адаптер

        * adapter - :py:class:`android.widget.SimpleExpandableListAdapter`

        .. code-block:: java

            expListView.setAdapter(adapter);


    .. py:method:: setOnChildClickListener(OnChildClickListener listener)

        Устанавливает слушателя на нажатие элемента

        * listener - :py:class:`android.widget.ExpandableListView.OnChildClickListener`

        .. code-block:: java

            expListView.setOnChildClickListener(new OnChildClickListener(){})


    .. py:method:: setOnGroupClickListener(OnGroupClickListener listener)

        Устанавливает слушателя на нажатие группы

        * listener - :py:class:`android.widget.ExpandableListView.OnGroupClickListener`

        .. code-block:: java

            expListView.setOnGroupClickListener(new OnGroupClickListener(){})


    .. py:method:: setOnGroupCollapseListener(OnGroupCollapseListener listener)

        Устанавливает слушателя на сворачивание группы

        * listener - :py:class:`android.widget.ExpandableListView.OnGroupCollapseListener`

        .. code-block:: java

            expListView.setOnGroupCollapseListener(new OnGroupCollapseListener(){})


    .. py:method:: setOnGroupExpandListener(OnGroupExpandListener listener)

        Устанавливает слушателя на разворачивание группы

        * listener - :py:class:`android.widget.ExpandableListView.OnGroupExpandListener`

        .. code-block:: java

            expListView.setOnGroupExpandListener(new OnGroupExpandListener(){})


OnChildClickListener
--------------------

.. py:class:: android.widget.ExpandableListView.OnChildClickListener()

    Интерфейс слушателя события клика элемента


    .. py:method:: onChildClick(ExpandableListView parent, View view, int groupPosition, int childPosition, long id)

        Обработчик


OnGroupClickListener
--------------------

.. py:class:: android.widget.ExpandableListView.OnGroupClickListener()

    Интерфейс слушателя события клика группы


    .. py:method:: onGroupClick(ExpandableListView parent, View view, int groupPosition, long id)

        Обработчик


OnGroupCollapseListener
-----------------------

.. py:class:: android.widget.ExpandableListView.OnGroupCollapseListener()

    Интерфейс слушателя события сворачивания группы

    .. py:method:: onGroupCollapse(int groupPosition)

        Обработчик


OnGroupExpandListener
---------------------

.. py:class:: android.widget.ExpandableListView.OnGroupExpandListener()

    Интерфейс слушателя события пазворачивания группы

    .. py:method:: onGroupExpand(int groupPosition)

        Обработчик

