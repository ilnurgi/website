Tk
==

.. py:class:: Tk()

    Основной объект, виджет, модуля, является основной формой, окном интерфейса.

    .. code-block:: py

        import tkinter as tk

        window = tk.Tk()

    .. py:method:: geometry(str)

        Устанавливает размеры окна, 'высотаХширина+Х+У'

        >>> window.geometry(u'100х100+10+10')


    .. py:method:: iconbitmap(path)

        Устанавливает иконку окна

        >>> window.title(u'key.ico')


    .. py:method:: mainloop()

        Отрисовывает форму

        >>> window.mainloop()


    .. py:method:: maxsize(height, width)

        Устанавливает максимальный размер окна

        >>> window.maxsize(1024, 786)


    .. py:method:: minsize(height, width)

        Устанавливает минимальный размер окна

        >>> window.minsize(124, 76)


    .. py:method:: title(text)

        Устанавливает заголовок окна

        >>> window.title(u'Заголовок')

    .. py:attribute:: menu

        Меню окна, объект Menu