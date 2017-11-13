OptionMenu
==========

.. py:class:: OptionMenu(widget, var, *list)

    Меню, список для выбора

    * widget - виджет для встраивания

    * var - переменная для установки

    * list - список для выбора

    .. code-block:: py

        s = StringVar(value='Красный')
        op = OptionMenu(window, s, *['Красный', 'Зеленый'])