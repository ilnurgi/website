Tk - базовый класс приложения
=============================

.. py:class:: Tk()

    Базовый класс приложения

    Наследник :py:class:`WM`,  :py:class:`Misk`

    .. code-block:: py

        from Tkinter import Tk, Menu

        # создаем наше приложение
        window = Tk()

        # создаем и добавляем меню, верхняя панель в приложение
        menu = Menu()
        window.config(menu=menu)

        # запускаем цикл обработки событий
        window.mainloop()


    .. py:attribute:: menu

        Меню окна, объект Menu


    .. py:method:: destroy()

        Закрывает приложение

        .. code-block:: py

            window.destroy()


    .. py:method:: eval(code_str)

        Выполнить строку на языке программирования tcl

        .. code-block:: py

            root.eval('package require tile; ttk::style theme use clam')
            root.eval('ttk::button .b -text {ttk button}; pack .b')


    .. py:method:: evalfile(file_path)

        Выполняет код, записанный в файл.


    .. py:method:: geometry(size)

        Устанавливает геометрию окна в формате ШИРИНАxВЫСОТА+Х+У.

        Если не заданы параметры, то возвращает текущие размеры и координаты.

        .. code-block:: py

            # поместить окно в точку с координатам 40,80 и установить размер в 600x400
            window.geometry("600x400+40+80")

            # только изменить размер
            window.geometry("600x400")

            # только переместить окно
            window.geometry("+40+80")

    .. py:method:: iconbitmap(path)

        Устанавливает иконку окна

        .. code-block:: py

            window.title(u'key.ico')


    .. py:method:: mainloop()

        Отрисовывает форму и запускает цикл обработки событий

        .. code-block:: py

            window.mainloop()