Treeview
========

.. py:class:: Treeview(widget, **kargs)

    Виджет, дерево

    :param widget: родительский виджет
    :param tuple columns: список колонок
    :param selectmode: tk.EXTENDED - множественный выбор, tk.BROWSE - выбор 1 строки, tk.NONE - без выбора вообще


    .. py:method:: column(tag, **kwargs)

        Добавляет в таблицу колонку

        :param tag: тег колонки
        :param str anchor: выравнивание содержимого ячеек
        :param int minwidth: минимальная ширина колонки
        :param int width: ширина колонки


    .. py:method:: heading(tag, **kwargs)

        Устанавливает заголовок столбца

        :param tag: тег колонки
        :param str text: заголовок колонки
        :param img: вставляет картинку в заголовок
        :type img: :py:class:`PhotoImage`


    .. py:method:: insert(tag, index, **kwargs)

        Добавляет в таблицу строку

        :param tag: тег строки, в которую добавляется новая строка
        :param index: индекс позиции, куда вставляется строка (tk.END)
        :param str text: заголовок строки
        :param tuple values: кортеж строк, значений
        :param img: вставляет картинку в строку
        :type img: :py:class:`PhotoImage`

    .. py:method:: selection()

        Возвращает кортеж id выделенных строк