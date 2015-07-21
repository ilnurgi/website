.. py:module:: QtGui

QDesktopWidget - объект, рабочий стол операционной системы
===========================================================

.. py:class:: QDesktopWidget()

    Данный объект можно получить методом :py:meth:`QtGui.QApplication.desktop()`

    Наследник :py:class:`QtGui.QWidget`


    .. py:method:: availableGeometry()

        Возвращает :py:class:`QtCore.QRect`, содержащий координаыт только доступной части экрана


    .. py:method:: height()

        Возвращает число, высоту всего экрана


    .. py:method:: screenGeometry()

        Возвращает :py:class:`QtCore.QRect`, содержащий координаыт всего экрана


    .. py:method:: width()

        Возвращает число, ширину всего экрана