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

    .. js:function:: Destroy()  
    
    .. js:function:: GetAbsHeight() 
    
    .. js:function:: GetAbsWidth()  
    
    .. js:function:: GetHeight()    
    
    .. js:function:: GetLineCount() 
    
    .. js:function:: GetLineStart( line )   
    
    .. js:function:: GetLineTop( line ) 
    
    .. js:function:: GetMaxLines()  
    
    .. js:function:: GetPosition()  
    
    .. js:function:: GetText()  
    
    .. js:function:: GetTextSize( mode )    
    
    .. js:function:: GetType()  Returns “Text”
    
    .. js:function:: GetVisibility()    
    
    .. js:function:: GetWidth() 
    
    .. js:function:: Release()  
    
    .. js:function:: SetBackColor( color )  
    
    .. js:function:: SetBackGradient( color1,color2,color3,p4,p5,p6,p7 )    
    
    .. js:function:: SetBackGradientRadial( x,y,r,color1,color2,color3,p7 ) 
    
    .. js:function:: SetBackground( imagefile,options ) 
    
    .. js:function:: SetEllipsize( mode )   Shorten long text with “…” mode=“Start”,“Middle”, “End” or “marq”
    
    .. js:function:: SetFontFile( file )    
    
    .. js:function:: SetHtml( html )    
    
    .. js:function:: SetMargins( left,top,right,bottom )    
    
    .. js:function:: SetOnLongTouch( callback ) 
    
    .. js:function:: SetOnTouch( callback ) 
    
    .. js:function:: SetOnTouchDown( callback ) 
    
    .. js:function:: SetOnTouchMove( callback ) 
    
    .. js:function:: SetOnTouchUp( callback )   
    
    .. js:function:: SetPadding( left,top,right,bottom )    
    
    .. js:function:: SetPosition( left,top,width,height )   
    
    .. js:function:: SetScale( x,y )    
    
    .. js:function:: SetSize( width,height )    
    
    .. js:function:: SetText( text )    
    
    .. js:function:: SetTextColor( color )  
    
    .. js:function:: SetTextShadow( radius,dx,dy,color )    
    
    .. js:function:: SetTextSize( size,mode )   
    
    .. js:function:: SetTouchable( touchable )  
    
    .. js:function:: SetVisibility( HideShow )
    
