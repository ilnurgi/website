QGridLayout
===========

.. py:class:: QGridLayout

    Контейнер для расположения элементов в сетке

    .. code-block:: py

        grid = QGridLayout()


    .. py:method:: addWidget(widget, row, col)

        Добавляет виджет в указанную ячейку сетки

        .. code-block:: py

            grid.addWidget(button_widget, 0, 0)


    .. py:method:: setSpacing(space)

        Задаем отсутпы внутри ячейки сетки

        .. code-block:: py

            grid.setSpacing(5)