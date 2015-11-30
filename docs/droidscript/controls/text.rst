Text - текстовое поле для ввода
===============================


.. js:class:: Text

    Текстовое поле для ввода, :js:func:`CreateText`

    Также имеет аналогичные методы:

        * :js:func:`GetHeight`

        * :js:func:`GetVisibility`

        * :js:func:`GetWidth`

        * :js:func:`SetBackgroud`

        * :js:func:`SetBackColor`

        * :js:func:`SetBackGradient`

        * :js:func:`SetBackGradientRadial`

        * :js:func:`SetMargins`

        * :js:func:`SetPadding`

        * :js:func:`SetPosition`

        * :js:func:`SetSize`

        * :js:func:`SetTouchable`

        * :js:func:`SetVisibility`


    .. js:function:: GetLineCount()

    .. js:function:: GetLineStart(lineNum)

    .. js:function:: GetLineTop(lineNum)

    .. js:function:: GetMaxLines()

    .. js:function:: GetText()

    .. js:function:: GetTextSize(mode)


    .. js:function:: SetEllipsize(mode)

        * `mode`

            * `start`
            * `middle`
            * `end`
            * `marq`

    .. js:function:: SetFontFile(file)


    .. js:function:: SetHtml(html)


    .. js:function:: SetOnTouch(callback)

        Устанавливает функцию обработчик нажатия на элемент, в обработчик передает эвент события

        .. code-block:: js
            
            txt.SetOnTouch(function(ev){});


    .. js:function:: SetOnLongTouch(callback)
    .. js:function:: SetOnTouchDown(callback)
    .. js:function:: SetOnTouchMove(callback)
    .. js:function:: SetOnTouchUp(callback)

        Устанавливает обработчик отрыва касания от элемента, в обработчик передается эвент события

        .. code-block:: js
            
            txt.SetOnTouchUp(finction(ev){});


    .. js:function:: SetText(text)


    .. js:function:: SetTextColor(colorCode)

    .. js:function:: SetTextShadow(radius, dx, dy, color)

        Задает тень, для объекта

        .. code-block:: js

            txt.SetTextShadow(2, 0, 1, 'red');
            
            

    .. js:function:: SetTextSize(size)

        Задает размер для текстового поля

        .. code-block:: js
            
            txt = app.CreateText('Hello');
            txt.SetTextSize(32);
