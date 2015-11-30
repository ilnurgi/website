Button - виджет кнопка
======================

.. js:class:: Button

    Кнопка, :js:func:`CreateButton`, :js:func:`GetLastButton`

    Также имеет аналогичные методы:

        * :js:func:`GetHeight`

        * :js:func:`GetText`

        * :js:func:`GetVisibility`

        * :js:func:`GetWidth`

        * :js:func:`SetFontFile`

        * :js:func:`SetHtml`

        * :js:func:`SetMargins`

        * :js:func:`SetOnTouch`

        * :js:func:`SetPadding`

        * :js:func:`SetPosition`

        * :js:func:`SetSize`

        * :js:func:`SetText`

        * :js:func:`SetTextColor`

        * :js:func:`SetTextShadow`

        * :js:func:`SetTextSize`

        * :js:func:`SetVisibility`


    .. js:function:: SetStyle(color1, color2, radius, borderColor, borderSize, shadow)

        Устанавливает стиль для объекта

        .. code-block:: js
            
            // устанавливает цвет фона
            btn.SetStyle('black');

            // устанавливает градиентную заливку фона
            btn.SetStyle('black', 'red')

            // с закрушленными углами
            btn.SetStyle('#4285f3', '#4285f4', 4)


    .. js:function:: Button.GetAbsHeight()   

    .. js:function:: Button.GetAbsWidth() 

    .. js:function:: Button.GetTextSize( mode )  

    .. js:function:: Button.GetType()    

    .. js:function:: Button.SetScale( x,y )  


