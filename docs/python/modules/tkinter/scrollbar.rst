Scrollbar - виджет, прокрутка
=============================


.. py:class:: Scrollbar(**kwargs)

    Виджет, прокрутка

    Наследник :ref:class:`Widget`

    * `elementborderwidth` -
    * `jump` -
    * `orient` -
    * `repeatdelay` -
    * `repeatinterval` -
    * `troughcolor` -
    * `width` -


    .. code-block:: py

        from Tkinter import Tk, Text, Scrollbar

        root = Tk()
        text = Text(root, height=3, width=60)
        text.pack(side='left')

        scrollbar = Scrollbar(root)
        scrollbar.pack()

        # первая привязка
        scrollbar['command'] = text.yview

        # вторая привязка
        text['yscrollcommand'] = scrollbar.set

        root.mainloop()


    .. py:method:: activate(index)
    .. py:method:: delta(deltax, deltay)
    .. py:method:: fraction(x, y)
    .. py:method:: identify(x, y)
    .. py:method:: get()
    .. py:method:: set(*args)