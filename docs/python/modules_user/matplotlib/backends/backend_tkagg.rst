.. py:module:: backend_tkagg

FigureCanvasTkAgg
=================

.. py:class:: FigureCanvasTkAgg()

    Рисует график на виджете tkinter

    .. code-block:: py

        fig = Figure()
        # ...
        canvas = FigureCanvasTkAgg(fig, frame)
        canvas.show()


.. py:class:: NavigationToolbar2TkAgg()

    Добавляет кнопки управления для канваса

    .. code-block:: py

        toolbar = NavigationToolbar2TkAgg(canvas, frame)
        toolbar.update()