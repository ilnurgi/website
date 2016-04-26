Style - стили виджетов
======================

.. py:class:: Style(master=None)

    Задает стили для всех виджетов приложения

    .. code-block:: py

        style = Style()
        style.theme_use('default')


    .. py:method:: configure(style, query_opt=None, **kw)

        Конфигурирует стили

        .. code-block:: py

            style.configure('TFrame', background='#333')


    .. py:method:: theme_use(themename=None)

        Задает тему для стиля