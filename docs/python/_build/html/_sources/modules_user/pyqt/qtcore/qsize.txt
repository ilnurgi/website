.. py:module:: QtCore

QSize - объект, задает размер
=============================

.. py:class:: QSize(h=-1, w=-1)
.. py:class:: QSize(qsize)

    :param int h: высота
    :param int w: ширина
    :param QtCore.QSize qsize: объект, размер

    Описывает координаты какого-то размера

    >>> s1 = QtCore.QSize(50, 20)
    >>> s2 = QtCore.QSize(10, 5)
    >>> s1 + s2
    PyQt4.QtCore.QSize(60, 25)
    >>> s1 - s2
    PyQt4.QtCore.QSize(40, 15)
    >>> s1 * 2.5
    PyQt4.QtCore.QSize(125, 50)
    >>> s1 / 2
    PyQt4.QtCore.QSize(25, 10)
    >>> s1 == s2    
    False
    >>> s1 != s2
    True


    .. py:method:: boundedTo(qsize)

        :param QtCore.QSize qsize: объект, размер

        Возвращает :py:class:`QtCore.QSize`, который содержит максимальную ширину и высоту из размеров.


    .. py:method:: height()

        Возвращает число, высоту


    .. py:method:: isEmpty()

        Возвращает истину/ложь, если высота или ширина меньше или равен нулю


    .. py:method:: isNull()

        Возвращает истину/ложь, высота и ширина равны нулю


    .. py:method:: isValid()

        Возвращает истину/ложь, высота больше или равно нулю


    .. py:method:: scale(qsize, scale_type)
    .. py:method:: scale(w, h, scale_type)

        :param int h: высота
        :param int w: ширина
        :param QtCore.QSize qsize: объект, размер

        Производит изменение размеров области

        В параметре `scale_type` могут быть указаны следующие атрибуты из класса :py:class:`QtCore.Qt`:

            1. IgnoreAspectRatio - 0 - непосредственно изменяет размеры без сохранения про­порций сторон;
            2. KeepAspectRatio - 1 - производится поnытка масштабирования старой области внутри новой области без нарушения проnорций;
            3. KeepAspectRatioByExpanding - 2- производится попытка полностью заполнить новую область без нарушения пропорций старой области.

        Если новая ширина или высота имеет значение 0, то размеры изменяются непосредст­венно без сохранения пропорций, вне зависимости от значения параметра `scale_type`.


    .. py:method:: setHeight(h)

        Задает ширину


    .. py:method:: setWidth(w)

        Задает высоту


    .. py:method:: transpose()

        Меняет местами значения


    .. py:method:: width()

        Возвращает число, ширину