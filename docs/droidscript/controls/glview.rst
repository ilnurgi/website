GLView - GL представление
=========================


.. js:class:: GLView

    :js:func:`CreateGKView`

    Также поддерживает следующие методы:

    * :js:func:`SetOnTouch`

    * :js:func:`SetOnTouchDown`

    * :js:func:`SetOnTouchMove`

    * :js:func:`SetOnTouchUp`

    * :js:func:`SetTouchable`


    .. js:attribute:: aspect

    .. js:function:: CreateImage(fileName, callback)

        Возвращает добавленную картинку в представление и вызывает обработчик

        .. code-block:: js
            
            glimage = glview.CreateImage('/sdcard/image.png', StartRender);

    
    .. js:function:: GetAbsHeight()

    .. js:function:: GetAbsWidth()

    .. js:function:: GetContext()

        Возвращает :js:class:`Context`, объект который похо на HTML5 canvas. Состояние предсталвения, с которым можно манипулировать

        .. code-block:: js
            
            context = glview.GetContext()


    
    .. js:function:: DrawImage(image, x, y, width, height, angle)

        Рисует изображение в представлении

        .. code-block:: js
            
            glview.DrawImage(glimage, x, y, width, height, angle)

    
    .. js:function:: DrawSprite( sheet, sx, sy, sw, sh, dx, dy, dw, dh )
    
    .. js:function:: Render()

        Рендерит представление

        .. code-block:: js

            glview.Render()
            

.. js:class:: Context

    Объект, похожий на HTML5 context, :js:func:`GetContext`


    .. js:function:: drawImage()


    .. js:function:: resetTransform()


    .. js:function:: restore()

    
    .. js:function:: rotate()


    .. js:function:: save()

        Сохраняет состояние, на которое можно вернуться


    .. js:function:: scale()


    .. js:function:: translate(x, y)


GLView.CreateImage( filename, callback)     
GLView.DrawImage(img, X, Y, width, height, angle)   
GLView.SetOnTouch(callback)     
GLView.DrawSprite(image, srcStartX, srcStartY, srcWidth, srcHeight,destX, destY, destWidth, destHeight)     
GLView.SetOnTouchUp( callback )     
GLView.SetOnTouchMove( callback )   
GLView.SetOnTouchDown( callback )   
GLView.SetTouchable( touchable )    
GLView.Render()     
GLView.GetContext()
    