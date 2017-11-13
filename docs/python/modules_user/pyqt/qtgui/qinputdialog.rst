QInputDialog
============

.. py:class:: QInputDialog()

    .. code-block:: py

        dialog = QInputDialog()


    .. py:staticmethod:: getText(parent_widget, title, message)

        Создает диалоговое окно ввода текста и возвращает введенный текст и состояние нажатия кнопки ОК.

        .. code-block:: py

            text, status = QInputDialog.getText(some_widget, 'title', 'message')