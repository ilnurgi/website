.. _android_widget_CheckBox:

android.widget.CheckBox
=======================

Кнопка, поддерживающая два состояния.

Представлена в виде отмеченного или неотмеченного флажка.


CheckBox
--------

.. py:class:: android.widget.CheckBox

    Наследник :ref:`android.view.View`.

    .. code-block:: java

        CheckBox myChb = (CheckBox) findViewById(R.id.myChb);

    .. py:method:: setChecked(bool)

        Установить флажок в указанное состояние

        .. code-block:: java

            myChb.setChecked(true);

    .. py:method:: isChecked()

        возвращает статус флажка