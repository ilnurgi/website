.. py:module:: tkinter

Frame
=====

Виджет, область для группировки


.. py:class:: Frame(**kwargs)

    Наследник :py:class:`Widget`

    * bg - :py:class:`str`, цвет фона
    
    * borderwidth, bd - :py:class:`int`, толщина границы
    
    * height - :py:class:`int`, высота виджета в пикселях

    * relief - :ref:`const_relief`

    * width - :py:class:`int`, высота виджета в пикселях

    .. code-block:: py

        frame = Frame(parent)


	.. pp:method:: place(**kwargs)

		Распологает виджет в указанной области

		* relwidht - относительная ширина, от 0 до 1

		* relheight - относительная высота, от 0 до 1

		* relx - относительная позиция левой линии, от 0 до 1
		
		* rely - относительная позиция верхней линии, от 0 до 1		
		
		* x - положение левого края

		* y - положение верхнего края
