Spinner
=======

.. js:class:: Spinner

    :js:class:`CreateSpinner`

    Также имеет аналогичные методы:

        * :js:func:`GetHeight`

        * :js:func:`GetText`

        * :js:func:`GetTextSize`

        * :js:func:`GetVisibility`

        * :js:func:`GetWidth`

        * :js:func:`SetMargins`

        * :js:func:`SetPadding`

        * :js:func:`SetPosition`

        * :js:func:`SetSize`

        * :js:func:`SetTextColor`

        * :js:func:`SetTextSize`

        * :js:func:`SetVisibility`       


    .. js:function:: GetTextSize( mode )

    .. js:function:: SelectItem( item )
    
    .. js:function:: SetList( list )
    
    .. js:function:: SetOnChange( callback )

        Устанавливает обработчик события, выбор элемента. В обработчик передается выбранный элемент.

        .. code-block:: js
            
            spin.SetOnChange(function(item){
                app.ShowPopup( "Selected = " + item );
            });

    .. js:function:: GetAbsHeight()  
    
    .. js:function:: GetAbsWidth()   
    
    .. js:function:: GetHeight() 
    
    .. js:function:: GetPosition()   
    
    .. js:function:: GetText()   
    
    .. js:function:: GetTextSize( mode ) 
    
    .. js:function:: GetType()   
    
    .. js:function:: GetVisibility() 
    
    .. js:function:: GetWidth()  
    
    .. js:function:: SelectItem( item )  See the info
    
    .. js:function:: SetBackColor( colorcode )   
    
    .. js:function:: SetBackGradient( p1,p2,p3,p4,p5,p6,p7 ) 
    
    .. js:function:: SetBackGradientRadial( p1,p2,p3,p4,p5,p6,p7 )   
    
    .. js:function:: SetList( list, p2 ) 
    
    .. js:function:: SetMargins( left,top,right,bottom ) 
    
    .. js:function:: SetOnChange( callback ) 
    
    .. js:function:: SetOnTouch( callback )  
    
    .. js:function:: SetPadding( left,top,right,bottom ) 
    
    .. js:function:: SetPosition( left,top,width,height )    
    
    .. js:function:: SetScale( x,y ) 
    
    .. js:function:: SetSize( width,height ) 
    
    .. js:function:: SetText( text ) 
    
    .. js:function:: SetTextColor( colorcode )   
    
    .. js:function:: SetTextSize( size,mode )    
    
    .. js:function:: SetVisibility( HideShow )
    
