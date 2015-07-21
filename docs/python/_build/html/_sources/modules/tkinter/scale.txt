Scale
=====

.. py:class:: Scale(widget, **kwargs)

    Виджет, позволяет устанавливать некоторое значение

    :param widget: родительский виджет
    :param from_: начальная позиция
    :param to: конечная позиция
    :param resolution: шаг
    :param label: подпись виджета
    :param int tickinterval: градуировка бегунка
    :param int sliderlength: длина бегунка
    :param orient: ориентация бегунка tk.HORIZONTAL
    :param length: длина бегунка

    .. py:method:: coords()

        Возвращает кортеж (х, у) положение слайдера относительно шкалы.