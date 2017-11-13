.. py:module:: QtGui

QApplication - приложение, с которого начинается построение интерфейса
======================================================================


.. py:class:: QApplication(*args)

    .. code-block:: py

        import sys

        from PyQt4.QtGui import QApplication, QWidget

        application = QApplication(sys.argv)
        
        w = QWidget()
        w.show()
        
        sys.exit(application.exec_())


    .. py:staticmethod:: clipboard()

        .. code-block:: py

            clipboard = QApplication.clipboard()


    .. py:staticmethod:: desktop()

        Возвращает объект :py:class:`QtGui.QDesktopWidget`, компонент рабочего стола.


    .. py:staticmethod:: focusWidget()

        Возвращает ссылку на компонент, находящийся в фокусе ввода.


    .. py:method:: argv()

        возвращает список переданных аргументов