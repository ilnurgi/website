.. py:module:: QtCore

QRect - объект, область
=======================

.. py:class:: QRect(x=0, y=0, w=0, h=0)
.. py:class:: QRect(qpoint, qsize)
.. py:class:: QRect(qpoint, qpoint2)
.. py:class:: QRect(qrect)

    :param int x: координата по оси х, левый верхний угол
    :param int y: координата по оис у, левый верхний угол
    :param int w: ширина области    
    :param int h: высота области
    :param QtCore.QPoint qpoint: точка левого верхнего угла
    :param QtCore.QPoint qpoint2: точка правого нижнего угла
    :param QtCore.QSize qsize: размер области
    :param QtCore.QRect qrect: объект, область

    Описывает координаты и размеры какой-то прямоуголной области

        >>> r1 = QtCore.QRect(O, О, 20, 20)
        >>> r2 = QtCore.QRect(10, 10, 20, 20)
        >>> r1 & r2
        PyQt4.QtCore.QRect(10, 10, 10, 10)
        >>> r1 | r2 
        PyQt4.QtCore.QRect(O, О, 30, 30)
        >>> r1 in r2
        False
        >>> r1 in QtCore.QRect(O, О, 30, 30)
        True
        >>> r1 == r2
        False
        >>> r1 != r2
        True

    .. py:method:: adjust(x1, y1, x2, y2)

        Сдвигает координаты левого верхнего и нижнего прва углов, относительно текущих значений

    
    .. py:method:: adjusted(x1, y1, x2, y2)

        Возвращает :py:class:`QtCore.QRect`, со смещенными координатами левого верхнего и нижнего прва углов, относительно текущих значений


    .. py:method:: bottom()

        Возвращает число, координату правого верхнего угла по оси у


    .. py:method:: bottomLeft()

        Возвращает число, координату левого нижнего угла


    .. py:method:: bottomRight()

        Возвращает число, координату правого нижнего угла


    .. py:method:: center()

        Возвращает координаты центра области

    
    .. py:method:: contains(x, y[, inherit=False])
    .. py:method:: contains(qpoint[, inherit=False])
    .. py:method:: contains(qrect[, inherit=False])

        :param QtCore.QPoint qpoint: точка левого верхнего угла
        :param QtCore.QRect qrect: область
        :param bool inherit: точка не должна лежать на границе

        Возвращает истину/ложь, если точка/область находится внутри области.


    .. py:method:: getCoords()

        Возвращает кортеж с координатами левого верхнего угла и правого нижнего угла


    .. py:method:: getRect()        

        Возвращает кортеж, с координатами левого верхнего угла и размерами области


    .. py:method:: height()

        Возвращает число, высоту объекта


    .. py:method:: intersect(qrect)

        :param QtCore.QRect qrect: область

        Возвращает :py:class:`QtCore.QRect`, область которая расположена на пересечении областей


    .. py:method:: intersected(qrect)

        :param QtCore.QRect qrect: область

        Возвращает :py:class:`QtCore.QRect`, область которая расположена на пересечении областей


    .. py:method:: intersects(qrect)

        :param QtCore.QRect qrect: область

        Возвращает истину/ложь, если области пересекаются


    .. py:method:: isEmpty()

        Возвращает истину/ложь, left() > right() или top() > bottom()


    .. py:method:: isNull()

        Возвращает истину/ложь, ширина и высота равны нулю


    .. py:method:: isValid()

        Возвращает истину/ложь, left() < right() и top() < bottom()


    .. py:method:: left()

        Возвращает число, координату левого верхнего угла по оси х

    
    .. py:method:: moveBottom(y)

        Перемещает координату х правого нижнего угла


    .. py:method:: moveBottomLeft(qpoint)

        :param QtCore.QPoint qpoint: точка

        Перемещает координаты левого нижнего угла


    .. py:method:: moveBottomRight(qpoint)

        :param QtCore.QPoint qpoint: точка

        Перемещает координаты правого нижнего угла


    .. py:method:: moveCenter(qpoint)

        :param QtCore.QPoint qpoint: точка

        Перемещает координаты центра


    .. py:method:: moveLeft(x)

        Перемещает координату х левого верхнего угла


    .. py:method:: moveRight(x)

        Перемещает координату х правого нижнего угла


    .. py:method:: moveTo(x, y)
    .. py:method:: moveTo(qpoint)

        :param int x: координата по оси х, левый верхний угол
        :param int y: координата по оис у, левый верхний угол
        :param QtCore.QPoint qpoint: точка левого верхнего угла

        Перемещает координаты левого верхнего угла


    .. py:method:: moveTop(y)

        Перемещает координату у левого верхнего угла


    .. py:method:: moveTopLeft(qpoint)

        :param QtCore.QPoint qpoint: точка

        Перемещает координаты левого верхнего угла


    .. py:method:: moveTopRight(qpoint)

        :param QtCore.QPoint qpoint: точка

        Перемещает координаты правого верхнего угла


    .. py:method:: normalized()

        Возвращает :py:class:`QtCore.QRect`, исправленный, если left() > right() или top() > bottom()


    .. py:method:: right()

        Возвращает число, координаты правого нижнего угла по оси х


    .. py:method:: setBottom(y)

        Задает координату правого нижнего угла по оси у


    .. py:method:: setBottomLeft(qpoint)

        :param QtCore.QPoint qpoint: точка

        Задает координату левого нижнего угла


    .. py:method:: setBottomRight(qpoint)

        :param QtCore.QPoint qpoint: точка

        Задает координату правого нижнего угла


    .. py:method:: setCoords(x1, y1, x2, y2)

        Задает координаты левого верхнего и правого нижнего углов


    .. py:method:: setHeight(h)

        Задает высоту области


    .. py:method:: setLeft(x)

        Задает координату левого верхнего угла по оси х


    .. py:method:: setRect(qrect)

        :param QtCore.QRect qrect: область

        Задает координату левого верхнего угла и размеры области


    .. py:method:: setRight(x)

        Задает координату правого нижнего угла по оси х


    .. py:method:: setSize(qsize)

        :param QtCore.QSize qsize: размер

        Задает размер области


    .. py:method:: setTop(y)

        Задает координату левого верхнего угла по оси y


    .. py:method:: setTopLeft(qpoint)

        :param QtCore.QPoint qpoint: точка

        Задает координату левого верхнего угла


    .. py:method:: setTopRight(qpoint)

        :param QtCore.QPoint qpoint: точка

        Задает координату правого верхнего угла


    .. py:method:: setX(x)

        Задает координату левого верхнего угла по оси х


    .. py:method:: setX(y)

        Задает координату левого верхнего угла по оси y


    .. py:method:: setWidth(w)

        Задает ширину области


    .. py:method:: size()

        Возвращает :py:class:`QtCore.QSize`, размер объекта

        
    .. py:method:: top()

        Возвращает число, координату левого верхнего угла по оси y


    .. py:method:: topLeft()

        Возвращает число, координату левого верхнего угла


    .. py:method:: topRight()

        Возвращает число, координату правого верхнего угла


    .. py:method:: translate(x, y)
    .. py:method:: translate(qpoint)

        :param int x: координата по оси х, левый верхний угол
        :param int y: координата по оис у, левый верхний угол
        :param QtCore.QPoint qpoint: точка

        Перемещает координаты левого верхнего угла относительно текущей


    .. py:method:: translated(x, y)
    .. py:method:: translated(qpoint)

        :param int x: координата по оси х, левый верхний угол
        :param int y: координата по оис у, левый верхний угол
        :param QtCore.QPoint qpoint: точка

        Возвращает :py:class:`QtCore.QRect`, с перемещенными координатами левого верхнего угла относительно текущей


    .. py:method:: unite(qrect)

        :param QtCore.QRect qrect: область

        Возвращает :py:class:`QtCore.QRect`, которая охватывает области


    .. py:method:: united(qrect)

        :param QtCore.QRect qrect: область

        Возвращает :py:class:`QtCore.QRect`, которая охватывает области


    .. py:method:: width()

        Возвращает число, ширину объекта


    .. py:method:: x()

        Возвращает число, координату левого верхнего угла по оси х


    .. py:method:: y()

        Возвращает число, координату левого верхнего угла по оси y