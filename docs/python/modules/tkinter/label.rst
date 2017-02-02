Label - виджет, надпись, без возможности редактирования.
========================================================

.. py:class:: Label(**kwargs)

    Надпись, виджет

    Наследник :py:class:`Widget`

    * bg - цвет фона
    * fg - цвет текста
    * height - высота виджета
    * image - изображение
    * state - константа :ref:`const_state`
    * width - ширина виджета

    .. code-block:: py

        label = Label(
            master,
            text="Some text",
            bg="black",
            fg="white",
        )