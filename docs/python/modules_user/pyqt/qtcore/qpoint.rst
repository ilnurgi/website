.. py:module:: QtCore

QPoint - объект, точка
======================

.. py:class:: QPoint(x=0, y=0)
.. py:class:: QPoint(qpoint)

    :param int x: координата х
    :param int y: координата у
    :param QtCore.QPoint qpoint: точка

    Описывает координаты какой-то точки

        >>> р1 = QtCore.QPoint(10, 20)
        >>> р2 = QtCore.QPoint(5, 9)
        >>> р1 + р2
        PyQt4.QtCore.QPoint(15, 29)
        >>> р1 - р2
        PyQt4.QtCore.QPoint(5, 11)
        >>> р1 * 2.5
        PyQt4.QtCore.QPoint(25, 50)
        >>> р1 / 2.0 
        PyQt4.QtCore.QPoint(5, 10)
        >>> -р1
        PyQt4:QtCore.QPoint(-10, -20)
        >>> р1 == р2
        Fa1se
        >>> р1 != р2
        True


    .. py:method:: isNull()

        Возвращает истину/ложь, координаты равны нулю


    .. py:method:: manhattanLength()

        Возвращает число, сумму абсолютных значений координат


    .. py:method:: setX(x)

        Задает координату по оси х


    .. py:method:: setX(y)

        Задает координату по оси y


    .. py:method:: x()

        Возвращает число, координату по оси х


    .. py:method:: y()

        Возвращает число, координату по оси у