.. py:module:: tkinter

Button - виджет кнопка
======================


.. py:class:: Button(**kwargs)

    Кнопка, виджет.

    Наследник :py:class:`Widget`

    * `command` - ссылка на функцию обработчика
    * `compound`
    * `default`
    * `height` - число, высота виджета, количесвто строк - для обычной кнопки, пиксели - для кнопки картинки
    * `image` - кнопка-картинка
    * `overrelief`
    * `state` - константа :ref:`const_state`
    * `width` - число, ширина виджета, количесвто символов - для обычной кнопки, пиксели - для кнопки картинки

    .. code-block:: py

        def click():
            print 'clicked'

        button = Button(command=click)
        button.pack()


    .. py:method:: flash()

        Вспышка кнопки, чередование активной и нормальной цветов.


    .. py:method:: invoke()

        Возвращает результат работы обработчика кнопки
