.. py:module:: QtGui

QLabel - виджет, надпись
========================

.. py:class:: QLabel(parent=0, f=0)
.. py:class:: QLabel(text, parent=0, f=0)

    * parent - :py:class:`QtGui.QWidget`, родительский виджет
    * f - флаги окна
    * text - :py:class:`QtCore.QString`, текст для виджета

    .. code-block:: py

        label = QtGui.QLabel('text')


    .. py:method:: setAlignment()

    .. py:method:: setTooltip(text)

        Задает всплывающую подсказку

        .. code-block:: py

            label.setTooltip('tooltip')