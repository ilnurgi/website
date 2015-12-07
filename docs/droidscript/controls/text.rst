Text - текстовое поле
=====================


.. js:class:: Text

    Текстовое поле, :js:func:`app.CreateText`

    .. js:function:: Destroy()

    .. js:function:: Focus()

    .. js:function:: GetAbsHeight()

    .. js:function:: GetAbsWidth()

    .. js:function:: GetHeight()

    .. js:function:: GetLineCount()

    .. js:function:: GetLineStart(lineNum)

    .. js:function:: GetLineTop(lineNum)

    .. js:function:: GetMaxLines()

    .. js:function:: GetPosition()

    .. js:function:: GetText()

    .. js:function:: GetTextSize(mode)

    .. js:function:: GetType()

    .. js:function:: GetVisibility()

    .. js:function:: GetWidth()

    .. js:function:: Release()

    .. js:function:: SetBackColor(colorCode)

    .. js:function:: SetBackGradient(color1,color2,color3,p4,p5,p6,p7)

    .. js:function:: SetBackGradientRadial(x,y,r,color1,color2,color3,p7)

    .. js:function:: SetBackground(imagefile,options)

    .. js:function:: SetEllipsize(mode)

        * `mode`

            * `start`

            * `middle`

            * `end`

            * `marq`


    .. js:function:: SetFontFile(fileName)

    .. js:function:: SetHtml(html)

    .. js:function:: SetMargins(left,top,right,bottom)

    .. js:function:: SetOnLongTouch(callback)

    .. js:function:: SetOnTouch(callback)

        Устанавливает функцию обработчик нажатия на элемент, в обработчик передается эвент события

        .. code-block:: js
            
            txt.SetOnTouch(txt_OnTouch);

            function txt_OnTouch(event){}


    .. js:function:: SetOnTouchDown(callback)

    .. js:function:: SetOnTouchMove(callback)

    .. js:function:: SetOnTouchUp(callback)

        Устанавливает функцию обработчик отпускания после нажатия на элемент, в обработчик передается эвент события

        .. code-block:: js
            
            txt.SetOnTouchUp(txt_OnTouchUp);

            function txt_OnTouchUp(event){}


    .. js:function:: SetPadding(left,top,right,bottom)

    .. js:function:: SetPosition(left,top,width,height)

    .. js:function:: SetScale(x,y)

    .. js:function:: SetSize(width,height)

    .. js:function:: SetText(text)

    .. js:function:: SetTextColor(colorCode)

    .. js:function:: SetTextShadow(radius, dx, dy, color)

        Задает тень, для объекта

        .. code-block:: js

            txt.SetTextShadow(2, 0, 1, 'red');


    .. js:function:: SetTextSize(size, mode)

        Задает размер для текстового поля

        .. code-block:: js

            txt.SetTextSize(32);


    .. js:function:: SetTouchable(touchable)

    .. js:function:: SetVisibility(HideShow)    
