Tk - базовый класс приложения
=============================

.. py:class:: Tk()

    Базовый класс приложения

    Наследник :py:class:`WM`,  :py:class:`Misk`

    .. code-block:: py

        from Tkinter import Tk

        # создаем наше приложение
        window = Tk()

        # запускаем цикл обработки событий
        window.mainloop()


    .. py:attribute:: menu

        Меню окна, объект Menu


    .. py:method:: bind(event_name, callback)

        Вешаем обработчик на событие

        * event_name - название события

            * "<Configure>" - изменение конфигурации окна

        .. code-block:: py

            def configure(event):
                """
                event.width
                event.height
                """

            window.bind('<Configure>', configure)


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

            # растянуть окно на весь экран
            window.geometry(
                '{width}x{height}+0+0'.format(
                    window.winfo_screenwidth(),
                    window.winfo_screenheight(),
                )
            )


    .. py:method:: iconbitmap(path)

        Устанавливает иконку окна

        .. code-block:: py

            window.title(u'key.ico')


    .. py:method:: mainloop()

        Отрисовывает форму и запускает цикл обработки событий

        .. code-block:: py

            window.mainloop()


    .. py:method:: maxsize()

        Возвращает кортеж, максимальная ширина и высота экрана

        .. code-block:: py

            window.maxsize()
            (1920, 1080)


    .. py:method:: minsize([w, h])

        Возвращает или устанавливает минимальный размер окна

        .. code-block:: py

            window.minsize()
            # (100, 100)

            window.minsize(200, 200)


    .. py:method:: winfo_height()

        Возвращает число, текущую ширину окна

        .. code-block:: py

            window.winfo_height()
            # 1


    .. py:method:: winfo_width()

        Возвращает число, текущую ширину окна

        .. code-block:: py

            window.winfo_width()
            # 1


    .. py:method:: winfo_screenheight()

        Возвращает число, высоту экрана

        .. code-block:: py

            window.winfo_screenheight()
            # 1080


    .. py:method:: winfo_screenwidth()

        Возвращает число, ширина экрана 

        .. code-block:: py

            window.winfo_screenwidth()
            # 1920


    .. py:method:: wm_state(state)

        Задает состояние для окна

        * zoomed - растянуть на весь экран

        .. code-block:: py

            window.wm_state('zoomed')


