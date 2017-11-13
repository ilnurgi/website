.. py:module:: QtGui

QVBoxLayout - слой, вертикальный контейнер
==========================================

Виджеты внутри этого контейнера будут распологаться вертикально.


.. py:class:: QVBoxLayout()

    Контейнер виджетов

    .. code-block:: py

        layout = QVBoxLayout()


    .. py:method:: addSpacing(space)

        Добавляет пустое место в контейнер

        .. code-block:: py

            layout.addSpacing(100)


    .. py:method:: addWidget(widget, alignment)

        Добавляет виджет в лейаут

        * widget - :py:class:`QtGui.QWidget`, виджет
        * alignment - положение виджета в контейнере
            * :py:attr:`QtCore.Qt.QAlignTop`
            * :py:attr:`QtCore.Qt.QAlignBottom`


        .. code-block:: py

            button = QPushButton('text')

            layout.addWidget(button)


    .. py:method:: insertSpacing(index, space)

        Добавляет пустое место в контейнер по указанному индексу

        .. code-block:: py

            layout.insertSpacing(0, 150)


    .. py:method:: insertWidget(index, widget)

        Добавляет виджет в контейнер по указанной позиции

        .. code-block:: py

            layout.insertWidget(0, button_widget)