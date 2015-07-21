Entry
=====

.. py:class:: Entry(widget, **kwargs)

    Поле ввода, виджет

    :param widget: родительский виджет

    .. py:method:: delete(start, end)

        Очищает поле ввода

        :param int start: начальная позиция
        :param end: конечная позиция (tk.END)

    .. py:method:: insert(start, text)

        Вставляет текст в поле

        :param int start: позиция вставки
        :param str text: текст