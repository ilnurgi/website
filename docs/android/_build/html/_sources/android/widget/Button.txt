.. _android_widget_Button:

android.widget.Button
=====================

.. py:class:: android.widget.Button

    Наследник :ref:`android.view.View`. Стандартная кнопка.

    .. py:method:: setText(str)
    .. py:method:: setText(R.string.name)

        устанавливает текст для объекта

    .. py:method:: setEnabled(bool)

        активность кнопки

    .. py:method:: setOnClickListener(callback)

        устанавливает обработчик нажатия кнопки

        :param callback: :ref:`android_view_View_OnClickListener`