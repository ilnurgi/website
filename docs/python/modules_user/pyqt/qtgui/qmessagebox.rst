.. py:module:: QtGui

QMessageBox
===========


.. py:class::QMessageBox()


    .. py:staticmethod:: question(parent, title, message, *args)

        Создает окно с запросом, и вовзращает результат

        .. code-block:: py

            reply = QMessageBox.question(parent_widget, 'Title', 'message', QMessageBox.Yes, QMessageBox.No)

            print(reply == QMessageBox.Yes)
            print(reply == QMessageBox.No)