List
====


.. js:class:: List

    :js:func:`CreateList`

    Также имеет аналогичные методы:
        
        * :js:func:`GetTextSize`
        
        * :js:func:`GetHeight`
        
        * :js:func:`GetWidth`
        
        * :js:func:`GetVisibility`
        
        * :js:func:`SetBackColor`
        
        * :js:func:`SetBackGradient`
        
        * :js:func:`SetBackGradientRadial`
        
        * :js:func:`SetBackground`
        
        * :js:func:`SetFontFile`
        
        * :js:func:`SetEllipsize`
        
        * :js:func:`SetMargins`
        
        * :js:func:`SetOnTouch` - в обработичк передаются 4 параметра: title, body, type, index
        
        * :js:func:`SetOnLongTouch` - в обработичк передаются 4 параметра: title, body, type, index
        
        * :js:func:`SetPadding`
        
        * :js:func:`SetPosition`
        
        * :js:func:`SetSize`
        
        * :js:func:`SetTextColor`
        
        * :js:func:`SetTextShadow`
        
        * :js:func:`SetTextSize`
        
        * :js:func:`SetVisibility`

    
    .. js:function:: AddItem( title, body, image )
    
    .. js:function:: GetList( delimeter )
    
    .. js:function:: RemoveItem( title )
    
    .. js:function:: SelectItem( name, body, scrollTo )
    
    .. js:function:: SelectItemByIndex( index, scroll )
    
    .. js:function:: SetEllipsize1( mode )
    
    .. js:function:: SetEllipsize2( mode )
    
    .. js:function:: SetHiTextColor1( colorCode )
    
    .. js:function:: SetHiTextColor2( colorCode )
    
    .. js:function:: SetDivider( height, color )
    
    .. js:function:: SetItem( title, newTitle, newBody, newImage )
    
    .. js:function:: SetList( list, delimeter )
    
    .. js:function:: SetTextColor1( colorCode )
    
    .. js:function:: SetTextColor2( colorCode )
    
    .. js:function:: SetTextMargins( left, top, right, bottom )
    
    .. js:function:: SetTextShadow1( radius, dx, dy, color )
    
    .. js:function:: SetTextShadow2( radius, dx, dy, color )
    
    .. js:function:: ScrollToItem( name, body )


ListView.AddItem( title,body,image )    
ListView.GetAbsHeight()     
ListView.GetAbsWidth()  
ListView.GetHeight()    
ListView.GetItemByIndex( index )    
ListView.GetLength()    
ListView.GetList( delimeter )   string = list.GetList(“,”);
List.GetList() with no params returns object list
ListView.GetPosition()  
ListView.GetTextSize( mode )    
ListView.GetType()  
ListView.GetVisibility()    
ListView.GetWidth()     
ListView.InsertItem(index,title,body,image)     
ListView.RemoveAll()    
ListView.RemoveItem( title )    
ListView.RemoveItemByIndex( index )     
ListView.ScrollToItem( name,body )  
ListView.ScrollToItemByIndex( index )   
ListView.SelectItem( title,body,scrollTo )  
ListView.SelectItemByIndex( index,scroll )  index is a number,
scroll could be true or false
ListView.SetBackColor( colorCode )  
ListView.SetBackGradient( color1,color2,color3,p4,p5,p6,p7 )    
ListView.SetBackGradientRadial( x,y,r,color1,color2,color3,p7 )     
ListView.SetBackground( imagefile,options )     
ListView.SetDivider( height,color )     
ListView.SetEllipsize( mode )   
ListView.SetEllipsize1( mode )  
ListView.SetEllipsize2( mode )  
ListView.SetFontFile( file )    
ListView.SetHiTextColor1( colorCode )   
ListView.SetHiTextColor2( colorCode )   
ListView.SetItem( title,newTitle,newBody,newImage )     
ListView.SetItemByIndex( index,newTitle,newBody,newImage )  
ListView.SetList( list,delimeter )  
ListView.SetMargins( left,top,right,bottom )    
ListView.SetOnLongTouch( callback )     sets the function called when list is long-touched
ListView.SetOnTouch( callback )     sets the function called when list is touched
ListView.SetPadding( left,top,right,bottom )    
ListView.SetPosition( left,top,width,height )   
ListView.SetScale( x,y )    
ListView.SetSize( width,height )    
ListView.SetTextColor( colorCode )  
ListView.SetTextColor1( colorCode )     
ListView.SetTextColor2( colorCode )     
ListView.SetTextMargins( left,top,right,bottom )    
ListView.SetTextShadow( radius,dx,dy,color )    
ListView.SetTextShadow1( radius,dx,dy,color )   
ListView.SetTextShadow2( radius,dx,dy,color )   
ListView.SetTextSize( size,mode )   
ListView.SetVisibility( ShowHide 