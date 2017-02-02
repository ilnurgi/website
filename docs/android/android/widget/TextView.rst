.. py:module:: android.widget

TextView - текстовое поле
=========================

.. py:class:: TextView([context[, attrs, [defStyle]]])

    Поддерживает многострочное отображение,
    форматирование и автоматический перенос слов и символов.

    Наследник :py:class:`android.view.View`

    * context - :py:class:`android.content.Context`

    * attrs - :py:class:`android.util.AttributeSet`

    * defStyle - int

    .. code-block:: java

        TextView txtPassword = (TextView)findViewById(R.id.txtPassword);


    .. py:method:: getText()
    
        Возвращает текст виджета

    .. py:method:: setText(text)

        Устанавливает текст виджета

        .. code-block:: java

            txtResult.setText(txtPassword.getText());

            txtResult2.setText(R.string.name);


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