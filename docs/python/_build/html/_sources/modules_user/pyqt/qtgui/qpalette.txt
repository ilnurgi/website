.. py:module:: QtGui

QPalette - палитра
==================

.. py:class:: QPalette()

    
    .. py:method:: setBrush([<состояние>, ]<роль>, qbrush)

        * `состояние` - состояние компонента

            * Active, Normal - компонент активен, находится в фокусе ввода
            * Disabled - компонент недоступен
            * Inactive - компонент неактивен, находится вне фокуса ввода

        * `роль` - указывается для какого элемента изменяется цвет

            * Window - цвет фона
            * Backgound - цвет фона
            * WindowText - цвет текста
            * Foreground - цвет текста

        ::

            pal = window.palette()
            pal.setBrush(
                QtGui.QPalette.Normal, 
                QtGui.QPalette.Window,
                QtGui.QBrush(
                    QtGui.QColor("#008800"), 
                    QtCore.Qt.SolidPattern))


    .. py:method:: setColor([<состояние>, ]<роль>, qcolor)

        Задает цвет для компонента

        * `состояние` - состояние компонента

            * Active, Normal - компонент активен, находится в фокусе ввода
            * Disabled - компонент недоступен
            * Inactive - компонент неактивен, находится вне фокуса ввода

        * `роль` - указывается для какого элемента изменяется цвет

            * Window - цвет фона
            * Backgound - цвет фона
            * WindowText - цвет текста
            * Foreground - цвет текста

        * `qcolor` - :py:class:`QtCore.QColor`, :py:class:`QtCore.Qt`

        ::

            pal.setColor(
                QtGui.QPalette.Normal, 
                QtGui.QPalette.Window,
                QtGui.QColor("#OOBBOO"))

