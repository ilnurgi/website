.. py:module:: pygal

Bar
===

.. py:class:: Bar()

    Гистограмма


    .. code-block:: py

        bar = Bar()


    .. py:attribute:: title

        Заголовок гистограммы

        .. code-block:: py

            bar.title = 'title'


    .. py:attribute:: x_labels

        Надписи на оси

        .. code-block:: py

            bar.x_labels = ['1', '2', '3', '4', '5', '6']


    .. py:attribute:: x_title

        Заголовок оси

        .. code-block:: py

            bar.x_title = 'X Title'


    .. py:attribute:: y_labels

        Надписи на оси

        .. code-block:: py

            bar.y_labels = ['1', '2', '3', '4', '5', '6']


    .. py:attribute:: y_title

        Заголовок оси

        .. code-block:: py

            bar.y_title = 'y Title'


    .. py:method:: add()

        Добавляет данные для гистограммы

        .. code-block:: py

            bar.add('?', [1, 2, 3, 4, 5, 6, ....])


    .. py:method:: render_to_file(file_path)

        Рендерит данные в файл

        .. code-block:: py

            bar.render_to_file('svg.svg')