ImageGrid
=========

.. js:class:: ImageGrid

    .. code-block:: js
        
        app.LoadPlugin( "ImageGrid" );
        grid = app.CreateImageGrid( list, width, height, cols, rows, cacheSize, options );


    .. js:function:: AddItem( name )
    
    .. js:function:: GetLength()
    
    .. js:function:: InsertItem( index, name )
    
    .. js:function:: RemoveAll()
    
    .. js:function:: RemoveItemByIndex( index )
    
    .. js:function:: SetList( list, delim )
    
    .. js:function:: SetOnLongTouch( callback )
    
    .. js:function:: SetOnTouch( callback )
    
    .. js:function:: SetSpacing( width, height )
    
    .. js:function:: Focus()
    
    .. js:function:: GetAbsWidth()
    
    .. js:function:: GetAbsHeight()
    
    .. js:function:: GetWidth()
    
    .. js:function:: GetHeight()
    
    .. js:function:: GetPosition()
    
    .. js:function:: GetType()
    
    .. js:function:: GetVisibility()
    
    .. js:function:: SetVisibility( visibility )
    
    .. js:function:: SetPadding( left, top, right, bottom )
    
    .. js:function:: SetMargins( left, top, right, bottom )
    
    .. js:function:: SetBackground( imageFile, options )
    
    .. js:function:: SetBackColor( colorCode )
    
    .. js:function:: SetBackGradient( color1, color2, color3 )
    
    .. js:function:: SetBackGradientRadial( x, y, r, color1, color2, color3 )
    
    .. js:function:: SetPosition( left, top, width, height )
    
    .. js:function:: SetSize( width, height )
    
    .. js:function:: SetScale( width, height )
    
