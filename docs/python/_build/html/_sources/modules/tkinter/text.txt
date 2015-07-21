Text
====

.. py:class:: Text(widget, **kwargs)

    Виджет, многострочное текстовое поле. Поддерживает те же методы что и Entry, но индексы передаются в виде '1.0'

    :param widget: родительский виджет
    :param int height: высота виджета
    :param int width: ширина виджета

    .. py:method:: clipboard_clear()

        Очищает буфер обмена

    .. py:method:: clipboard_append(str)

        Добавляет в буфер текст


    .. py:method:: mark_set(type, pos)

        Устанавливает метку

        :parsam type: tk.INSERT
        :param str pos: позиция метки

        >>> t.mark_set(tk.INSERT, '2.5')
        >>> t.mark_set('first', '2.5')

    .. py:method:: tag_add(name, start, end)

        Добавляет тег в текст

        :param str name: название тега
        :param start: начало
        :param end: конец

        >>> t.tag_add('tag', tk.SEL_FIRST, tk.SEL_LAST)

    .. py:method:: tag_config(name, **kwargs)

        Конфигурирует тег

        :param str name: название тега
        :param str background: фон
        :param str foregraund: текст
        :param typle font: параметры шрифта

        >>> t.tag_config('tag', background='black', foregraund='red', font=('times', 14, 'italic'))

    .. py:method:: see(pos)

        Прокручивает текстовое поле до позиции
        
    .. py:method:: selection_get(selection)

        Конфигурирует тег

        :param str name: название тега
        :param str background: фон
        :param str foregraund: текст
        :param typle font: параметры шрифта

        >>> t.tag_config('tag', background='black', foregraund='red', font=('times', 14, 'italic'))

    .. py:attribute:: yview
    .. py:attribute:: xview