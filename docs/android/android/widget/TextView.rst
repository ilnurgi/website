.. _android_widget_TextView:

android.widget.TextView
=======================

.. py:class:: android.widget.TextView([context[, attrs, [defStyle]]])

    :param context: :ref:`androif_content_Context`
    :param attrs: :ref:`androif_util_AtributeSet`
    :param defStyle: int

    Наследник :ref:`android.view.View`. Стандартная метка, предназначенная для вывода текста. Она поддерживает многострочное отображение, форматирование и автоматический перенос слов и символов.

    .. py:method:: getText()
    
        возвращает текст виджета

    .. py:method:: setText(str)
    .. py:method:: setText(R.string.name)

        устанавливает текст для объекта

    .. py:method:: setTextSize(size)

        устанавливает размер текст для объекта

    .. py:method:: setTextColor(color)

        устанавливает цвет текст для объекта


    .. py:method:: onDraw(canvas)

        :param canvas: :ref:`android_graphics_Graphics`
        :rtype: void


    .. py:method:: onKeyDown(keyCode, keyEvent)

        :param keyCode: int
        :param keyEvent: :ref:`KeyEvent`
        :rtype: boolean


    .. py:method:: requestFocus()

        устанавливает фокус на виджет