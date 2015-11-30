Image
=====

.. js:class:: Image

    Картинка, :js:func:`CreateImage`, :js:func:`GetLastImage`

    Данный объект можно использовать и как холст, для рисования

    Также имеет аналогичные методы:

        * :js:func:`GetHeight`

        * :js:func:`GetVisibility`

        * :js:func:`GetWidth`

        * :js:func:`SetFontFile`

        * :js:func:`SetMargins`

        * :js:func:`SetOnTouch` - в обработчик передается эвент события

            .. code-block:: js
                
                img.SetOnTouch(function(event){
                    app.ShowPopup(event.action); // Down, Up, Move
                    app.ShowPopup(event.x); 
                    app.ShowPopup(event.y); 

                });

        * :js:func:`SetOnLongTouch`

        * :js:func:`SetOnTouchDown` - в обработчик передается эвент события

        * :js:func:`SetOnTouchMove`

        * :js:func:`SetOnTouchUp`

        * :js:func:`SetPadding`

        * :js:func:`SetPosition`

        * :js:func:`SetSize`

        * :js:func:`SetTextSize` - устанавливает цвет шрифта для рисования

        * :js:func:`SetTouchable`

        * :js:func:`SetVisibility`

    
    .. js:function:: GetAbsHeight()
    
    .. js:function:: GetAbsWidth()

    .. js:function:: GetPixelData( format, left, top, width, height )

    .. js:function:: Clear()

        Очищает изображение
    
    .. js:function:: DrawArc( x1, y1, x2, y2, start, sweep )

    .. js:function:: DrawCircle(x, y, radius)

        Рисует окружность, с цуказанным центром и радиусом

        .. code-block:: js
            
            img.DrawCircle(0.2, 0.2, 0.1);

    .. js:function:: DrawImage( image, x, y, w, h, angle )
    
    .. js:function:: DrawImageMtx( image, matrix )
    
    .. js:function:: DrawLine(x1, y1, x2, y2)

        Рисует линии по указанным точкам

        .. code-block:: js
            
            img.DrawLine(0.6, 0.2, 0.7, 0.95);


    .. js:function:: DrawPoint(x, y)   

        Рисует точку на изображении

        .. code-block:: js
             
             img.DrawPoint(0.5, 0.5);

    
    .. js:function:: DrawRectangle(x1, y1, x2, y2, ?)

        Рисует прямоугльник

        .. code-block:: js
            
            img.DrawRectangle(0.22, 0.7, 0.9, 0.88);
            img.DrawRectangle(0.22, 0.7, 0.9, 0.88, 0.03);

    
    .. js:function:: DrawText(text, x, y)

        Рисует текст на изображении, :js:func:`SetTextSize`    

        .. code-block:: js
            
            img.DrawText('Hello', 0.1, 0.8);
            

    .. js:function:: Move(x, y)

        Смешает изображение

        .. code-block:: js
            
            img.Move(0, 0.15);


    .. js:function:: Reset()

        Сбросить масштаб изображения до указанных

        .. code-block:: js
            
            img.Reset(1.0, 1.0);


    .. js:function:: Rotate(angle, pivotX, pivotY)

        Вращает изображение на указанныей градус, относительно укзанной точки экрана

        .. code-block:: js
            
            image.Rotate(3, 0.5, 0.5);

    
    .. js:function:: Save(fileName)

    .. js:function:: SetAlpha(alpha)

        .. code-block:: js
            
            img.SetAlpha(1.0);


    .. js:function:: SetAutoUpdate( onoff )

    .. js:function:: SetColor(colorCode)

        Заливает изображение указанным цветом

        .. code-block:: js
            
            img.SetColor('red');


    .. js:function:: SetImage(img, width, height)
    
    .. js:function:: SetLineWidth(width)

        Устанавливает размер линии для рисования

        .. code-block:: js
            
            img.SetLineWidth(2.5);


    .. js:function:: SetMaxRate(ms)

    .. js:function:: SetOnLoad(callback)
    
    .. js:function:: SetPaintColor( colorCode )

        Устанавливает цвет кисти для рисования

        .. code-block:: js
            
            img.SetPaintColor('blue');

    .. js:function:: SetPaintStyle(style)

        Устанавливает стиль линии для рисования: 

        * `Line` - замкнутые фигуры не будут залиты цветом

        .. code-block:: js
            
            img.SetPaintStyle('Line');

    
    .. js:function:: Scale(x, y)

        Масштабирует изображение

        .. code-block:: js
            
            img.Scale(0.3, 0.3);


    .. js:function:: Skew( x, y )

    .. js:function:: Transform( matrix )
    
    .. js:function:: Update()


Image.Clear()   
Image.Destroy()     
Image.Draw( func, p1, p2, p3, p4, p5, p6, p7 )  
Image.DrawArc( x1, y1, x2, y2, start, sweep )   
Image.DrawCircle( x,y,radius )  
Image.DrawImage( image, x, y, w, h, angle )     
Image.DrawImageMtx( image, matrix )     
Image.DrawLine( x1, y1, x2, y2 )    
Image.DrawPoint( x, y )     
Image.DrawRectangle( x1, y1, x2, y2 )   
Image.DrawText( txt, x, y )     
Image.GetAbsHeight()    
Image.GetAbsWidth()     
Image.GetHeight()   
Image.GetName()     
Image.GetPixelData( format, left, top, width, height )  format can be “rawbase64”, “pngbase64” or “jpgbase64”
Image.GetPosition()     returns an object with properties: left, top, width, height
Image.GetType()     
Image.GetVisibility()   
Image.GetWidth()    
Image.Move( x, y )  
Image.Release()     
Image.Reset()   
Image.Rotate( angle, pivotX, pivotY )   
Image.Save( fileName,quality )  quality parameter new since Vers 1.29
support for png files since Vers 1.29
Image.Scale( x, y )     
Image.SetAlpha( alpha )     
Image.SetAutoUpdate( onoff )    
Image.SetBackColor( colorCode )     
Image.SetBackGradient( color1,color2,color3,p4,p5,p6,p7 )   
Image.SetBackGradientRadial( x,y,r,color1,color2,color3,p7 )    
Image.SetBackground( imagefile,options )    
Image.SetColor( color )     
Image.SetFontFile( file )   
Image.SetImage( image,width,height,options )    
Image.SetLineWidth( width )     
Image.SetMargins( left,top,right,bottom )   
Image.SetMaxRate( ms )  Set the minimum amount of time (in ms) between OnTouchMove events
Image.SetName( p1 )     
Image.SetOnLoad( callback )     
Image.SetOnLongTouch( callback )    
Image.SetOnTouch( callback )    
Image.SetOnTouchDown( callback )    
Image.SetOnTouchMove( callback )    
Image.SetOnTouchUp( callback )  
Image.SetPadding( left, top, right, bottom )    
Image.SetPaintColor( color )    
Image.SetPaintStyle( style )    
Image.SetPosition( left, top, width, height )   
Image.SetScale( x,y )   Fract values (as usual): 1=original, -1=flip (mirror)
Image.SetSize( width, height )  
Image.SetTextSize( size )   
Image.SetTouchable( callback )  
Image.SetVisibility( HideShow )     
Image.Skew( p1,p2 )     
Image.Transform( matrix )   
Image.Update()  
Image.Update2() 