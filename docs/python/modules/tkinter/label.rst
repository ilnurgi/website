.. py:module:: tkinter

Label
=====

Виджет, надпись, без возможности редактирования

.. py:class:: Label(**kwargs)

    Наследник :py:class:`Widget`

    * bg - :py:class:`str`, цвет фона
    * fg - :py:class:`str`, цвет текста
    * height - :py:class:`int`, высота виджета
    * image - изображение
    * state - константа :ref:`const_state`
    * text - :py:class:`str`, текст надписи
    * textvariable - :py:class:`StringVar`, переменная связанная с виджетом
    * width - :py:class:`int`, ширина виджета

    .. code-block:: py

        label = Label(
            master,
            text="Some text",
            bg="black",
            fg="white",
        )

    .. code-block:: py

        from tkinter import StringVar

        current_path = StringVar(value='some_dir')
        Label(textvariable=current_path)

        # теперь при любом изменении значения current_path, оно обновится и в виджете

    .. py:method:: pack(side)

        Распологает виджет на родительском виджете

        * side

            * :py:attr:`tkinter.LEFT`
            * :py:attr:`tkinter.RIGHT`

        .. code-block:: py

            label.pack(side=LEFT)