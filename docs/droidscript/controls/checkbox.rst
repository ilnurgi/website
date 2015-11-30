CheckBox
========

.. js:class:: CheckBox()

    CheckBox, :js:func:`CreateCheckBox`

    Также имеет аналогичные методы:

        * :js:func:`GetHeight`

        * :js:func:`GetText`

        * :js:func:`GetVisibility`

        * :js:func:`GetWidth`

        * :js:func:`SetMargins`

        * :js:func:`SetOnTouch` - в обработчик передается состояние

            .. code-block:: js
                
                chkb.SetOnTouch(function(isChecked){
                    app.ShowPopup(isChecked); // true, false
                });

        * :js:func:`SetPadding`

        * :js:func:`SetPosition`

        * :js:func:`SetSize`

        * :js:func:`SetText`

        * :js:func:`SetTextColor`

        * :js:func:`SetTextSize`

        * :js:func:`SetVisibility`


    .. js:function:: GetChecked()

    .. js:function:: SetChecked(checked)

CheckBox.Destroy()  
CheckBox.GetAbsHeight()     
CheckBox.GetAbsWidth()  
CheckBox.GetChecked()   
CheckBox.GetHeight()    
CheckBox.GetPosition()  
CheckBox.GetText()  
CheckBox.GetTextSize( mode )    
CheckBox.GetType()  
CheckBox.GetVisibility()    
CheckBox.GetWidth()     
CheckBox.Release()  
CheckBox.SetBackColor( colorCode )  
CheckBox.SetBackGradient( color1,color2,color3,p4,p5,p6,p7 )    
CheckBox.SetBackGradientRadial( x,y,r,color1,color2,color3,p7 )     
CheckBox.SetBackground( imagefile,options )     
CheckBox.SetChecked( checked )  
CheckBox.SetMargins( left,top,right,bottom )    
CheckBox.SetOnTouch( callback )     
CheckBox.SetPadding( left, top, right, bottom )     
CheckBox.SetPosition( left, top, width, height )    
CheckBox.SetScale( x,y )    
CheckBox.SetSize( width, height )   
CheckBox.SetText( text )    
CheckBox.SetTextColor( colorCode )  
CheckBox.SetTextSize( size,mode )   
CheckBox.SetVisibility( HideShow ) 