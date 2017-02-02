android.widget.GridView
=======================

XML
---

.. code-block:: xml

    <GridView

        android:layout_width="match_parent"
        android:layout_height="wrap_content"

        android:id="@+id/greedView" />


GridView
--------

.. py:class:: android.widget.GridView()

    Выводит элементы в виде сетки

    .. code-block:: java

        GridView gridView = (GridView) findViewById(R.id.gridView);


    .. py:attribute:: AUTO_FIT

        Константа, определяет количество столбцов


    .. py:attribute:: NO_STRETCH
    .. py:attribute:: STRETCH_COLUMN_WIDTH
    .. py:attribute:: STRETCH_SPACING
    .. py:attribute:: STRETCH_SPACING_UNIFORM


    .. py:method:: setColumnWidth(inw width)

        Задает ширину столбцов


    .. py:method:: setHorizontalSpacing(int space)

        Задает горизонтальный отступ между колоннами


    .. py:method:: setNumColumns(int numColumns)

        Задает количество столбцов

        .. code-block:: java

            gridView.setNumColumns(3);
            gridView.setNumColumns(GridView.AUTO_FIT);


    .. py:method:: setVerticalSpacing(int space)

        Задает вертикальный отступ между строками


    .. py:method:: setStretchMode(mode)

        Задает вертикальный отступ между строками

        * mode

            * NO_STRETCH - свободное пространство не используется
            * STRETCH_COLUMN_WIDTH – свободное пространство используется столбцами, это режим по умолчанию
            * STRETCH_SPACING – свободное пространство равномерно распределяется между столбцами
            * STRETCH_SPACING_UNIFORM – свободное пространство равномерно распределяется не только между столбцами, но и справа и слева
