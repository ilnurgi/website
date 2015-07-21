Listbox
=======

.. py:class:: Listbox(widget, **kwargs)

    Невыпадающий список, виджет.

    :param widget: родительский виджет
    :param selectmode: tk.BROWSE, tk.SINGLE, tk.MULTIPLE, tk.EXTENDED


    .. py:method:: curselection()

        Возвращает кортеж, выбранных значений

    .. py:method:: get(index)

        Возвращает элемент по индексу. (tk.ACTIVE)

    .. py:method:: insert(pos, str)

        Добавляет в виджет элемент

