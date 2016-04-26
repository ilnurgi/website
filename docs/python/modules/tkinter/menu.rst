Menu - виджет, навигационное меню
=================================


.. py:class:: Menu(**kwargs)

    Навигационное меню

    Наследник :py:class:`Widget`

    * `activeborderwidth` - число, ширина границ активного элемента
    * `activeforeground` - строка, цвет активного текста
    * `postcommand` - обработчик
    * `selectcolor` - строка, цвет выбранного элемента
    * `tearoff` -
    * `tearoffcommand` -
    * `title` -
    * `type` -

    .. code-block:: py

        menu = Menu()


    .. py:method:: add(itemType, cnf={}, **kwargs)

        Добавляет специфичный элемент в меню


    .. py:method:: add_command(label, command)

        Добавляет элемент в меню

        .. code-block:: py

            menu.add_command('about', about_callback)


    .. py:method:: add_cascade(cnf={}, **kwargs)

        Добавляет подменю :py:class:`Menu` в меню

        * `label` - надптсь кнопки
        * `menu` - :py:class:`Menu`
        * `underline` - булево, подчеркивание надписи

        .. code-block:: py

            cascade_menu = Menu()
            menu.add_cascade('other', cascade_menu)


    .. py:method:: add_checkbutton(label, variable, command)

        Добавляет флажок в меню


    .. py:method:: add_radiobutton(label, value, variable, command)

        Добавляет радиокнопку в меню


    .. py:method:: add_separator()

        Добавляет разделитель

        .. code-block:: py

            menu.add_separator()


    .. py:method:: delete(index1, index2=None)

        Удаляет элемента по индексу


    .. py:method:: entryconfig(index, **kwargs)
    .. py:method:: entryconfigure(index, **kwargs)

        Изменяет указанный элемент в меню


    .. py:method:: index(item)

        Возвращает индекс элемента виджета


    .. py:method:: insert_cascade(label, menu)

        Добавляет подменю в меню


    .. py:method:: insert_checkbutton(label, variable, command)

        Добавляет флажок в меню


    .. py:method:: insert_command(label, command)

        Добавляет элемент в меню


    .. py:method:: insert_radiobutton(label, value, variable, command)

        Добавляет радиокнопку в меню


    .. py:method:: insert_separator(index)

        Добавляет разделитель


    .. py:method:: invoke(index)

        Возвращает результат обработчика


    .. py:method:: post(x, y)

        Рисует меню в указанной позиции

        .. code-block:: py

            menu.post(1, 1)


    .. py:method:: type(index)

        Возвращает тип элемента по индексу (cascade, checkbutton, command, radiobutton, separator, tearoff)


    .. py:method:: unpost()

        Скрывает меню