ButtonToggle
============

.. js:class:: ButtonToggle()

    :js:func:`CreateToggle`, :js:func:`GetLastToggle`

    Также имеет аналогичные методы:

        * :js:func:`GetChecked`

        * :js:func:`GetHeight`

        * :js:func:`GetText`

        * :js:func:`GetTextSize`

        * :js:func:`GetVisibility`

        * :js:func:`GetWidth`

        * :js:func:`SetChecked`

        * :js:func:`SetMargins`

        * :js:func:`SetOnTouch` - в обработчик передается состояние

            .. code-block:: js
                
                btn.SetOnTouch(function(event){
                    app.ShowPopup(event.action); // Down, Up, Move
                    app.ShowPopup(event.x); 
                    app.ShowPopup(event.y); 

                });

        * :js:func:`SetPadding`

        * :js:func:`SetPosition`

        * :js:func:`SetSize`

        * :js:func:`SetText`

        * :js:func:`SetTextColor`

        * :js:func:`SetTextSize`

        * :js:func:`SetVisibility` 

    .. js:function:: Destroy()  
    
    .. js:function:: GetAbsHeight() 
    
    .. js:function:: GetAbsWidth()  
    
    .. js:function:: GetChecked()   
    
    .. js:function:: GetHeight()    
    
    .. js:function:: GetPosition()  
    
    .. js:function:: GetText()  
    
    .. js:function:: GetTextSize( mode )    
    
    .. js:function:: GetType()  
    
    .. js:function:: GetVisibility()    
    
    .. js:function:: GetWidth() 
    
    .. js:function:: SetChecked( checked )  
    
    .. js:function:: SetMargins( left,top,right,bottom )    
    
    .. js:function:: SetOnTouch( callback ) 
    
    .. js:function:: SetPadding( left, top, right, bottom ) 
    
    .. js:function:: SetPosition( left, top, width, height )    
    
    .. js:function:: SetScale( x,y )    
    
    .. js:function:: SetSize( width, height )   
    
    .. js:function:: SetText( text )    
    
    .. js:function:: SetTextColor( colorCode )  
    
    .. js:function:: SetTextSize( size,mode )   
    
    .. js:function:: SetVisibility( HideShow )
    
