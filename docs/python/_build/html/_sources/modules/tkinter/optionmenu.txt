OptionMenu
==========

.. py:class:: OptionMenu(widget, var, *list)

    Меню, список для выбора

    :param widget: виджет для встраивания
    :param var: переменная для установки
    :param list: список для выбора

    .. code-block:: py

        s = tk.StringVar()
        s.set(u'Красный')
        lis = [u'Красный', u'Зеленый']
        sp = tk.OptionMenu(window, s, *lis)