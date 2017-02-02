.. _android_widget_Toast:

android.widget.Toast
====================

.. py:class:: android.widget.Toast

    Всплывающее сообщение

    .. py:staticmethod:: makeText(context, message, duration)

        Статический метод, который возвращает объект, всплывающее сообщение,
        :py:class:`android.widget.Toast`

        * context - контекст приложения
        * message - сообщение
        * duration - прдолжительность вывода

            * Toast.LENGTH_LONG
            * Toast.LENGTH_SHORT

        .. code-block:: java

            Toast toast = Toast.makeText(
                getApplicationContext(),
                "some message",
                Toast.LENGTH_LONG);

    .. py:attribute:: LENGTH_LONG

        Статическая константа, продолжительность показа

    .. py:attribute:: LENGTH_SHORT

        Статическая константа, продолжительность показа

    .. py:method:: show()

        Отображает всплывающее сообщение