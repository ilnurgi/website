.. _android_widget_Toast:

android.widget.Toast
====================

.. py:class:: android.widget.Toast

    всплывающее сообщение

    .. py:staticmethod:: makeText(context, text, duration)

        :param context: ???
        :param text: :ref:`String`
        :param duration: продолжительность (Toast.LENGTH_LONG, Toast.LENGTH_SHORT)

        возвращает объект, всплывающее сообщение, которое потом необходимо отобразить через метод `show()`

    :: 

        Toast.makeText(this, "123", Toast.LENGTH_LONG).show();

    .. py:attribute:: LENGTH_LONG

        константа времени

    .. py:attribute:: LENGTH_SHORT

        константа времени