Menu
====

.. py:class:: Menu(widget, **kwargs)

    :param widget: родительский виджет
    :param bool tearof: отображает линию отрыва

    .. py:method:: add_command(label, command)

        Добавляет элемент в меню

    .. py:method:: add_separator()

        Добавляет разделитель

    .. py:method:: add_cascade(label, menu)

        Добавляет подменю в меню

    .. py:method:: add_checkbutton(label, variable, command)

        Добавляет флажок в меню

    .. py:method:: add_radiobutton(label, value, variable, command)

        Добавляет радиокнопку в меню

    .. py:method:: insert_checkbutton(label, variable, command)

        Добавляет флажок в меню

    .. py:method:: insert_radiobutton(label, value, variable, command)

        Добавляет радиокнопку в меню

    .. py:method:: insert_command(label, command)

        Добавляет элемент в меню

    .. py:method:: insert_separator()

        Добавляет разделитель


    .. py:method:: insert_cascade(label, menu)

        Добавляет подменю в меню