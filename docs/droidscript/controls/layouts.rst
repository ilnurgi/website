Layout - контейнер
==================


.. js:class:: Layout

    Контейнер. :js:func:`CreateLayout`      


    .. js:function:: AddChild(child, order)


    .. js:function:: Animate(type, callback)

        Анимирует компонент

        * `type`

            * `SlideFromLeft` - элемент появляется слева
            
            * 'SlideToLeft' - прячет элемент вправо

            * `SlideFromLeft` -  
            * `ScaleFromLeft` -  
            * `SlideToLeft` -  
            * `ScaleToLeft` -  
            * `SlideFromRight` -  
            * `ScaleFromRight` -  
            * `SlideToRight` -  
            * `caleToRight` -  
            * `SlideFromTop` -  
            * `ScaleFromTop` -  
            * `SlideToTop` -  
            * `ScaleToTop` - 
            * `SlideFromBottom` -  
            * `ScaleFromBottom` -  
            * `SlideToBottom` -  
            * `ScaleToBottom` - 

        .. code-block:: js
            
            lay.Animate('SlideToLeft');


    .. js:function:: ChildToFront(child)

        Устанавливает дочернии компонент на передний план план

        .. code-block:: js
            
            lay.ChildToFront(img1)


    .. js:function:: Destroy()

    .. js:function:: DestroyChild(child)

    .. js:function:: GetAbsHeight()

    .. js:function:: GetAbsWidth()

    .. js:function:: GetChildOrder(child)

        Возвращает 0 или 1, дочерний объект на переднем плане

        .. code-block:: js
            
            order = lay.GetChildOrder(child)


    .. js:function:: GetHeight()

    .. js:function:: GetPosition()

    .. js:function:: GetType()

    .. js:function:: GetVisibility()

        Возвращает строку, 'Hide', 'Show', 'Gone', видимость контейнера


    .. js:function:: GetWidth()


    .. js:function:: Release()

    .. js:function:: RemovaChild(child)


    .. js:function:: SetBackground(imageFile, options)

        Устанавливает картинку, в качестве фона

        .. code-block:: js
            
            lay.SetBackground('/Sys/Img/Blue.png');
            lay.SetBackground( "/res/drawable/pattern_carbon", "repeat" );


    .. js:function:: SetBackColor(colorCode)

        Устанавливает цвет фона для компонента.

        Цвета задаются как в 16-ричной форме, так и обычныой строкой: `black, white`

        .. code-block:: js
            
            lay.SetBackColor('#ff00ff00');


    .. js:function:: SetBackGradient(colorCode1, colorCode2, colorCode3, p4, p5, p6, p7)

        Устанавливает линейную градиентную заливку фона
        
        This sets 3 Background Colors for the Layout which are splited at a Line between p4 and p5 or between p6 and p7


    .. js:function:: SetBackGradientRadial(x, y, radius, colorCode1, colorCode2, colorCode3, p7)

        Устанавливает круговую градиентную заливку фона


    .. js:function:: SetBackgroud(image, options)

    .. js:function:: SetMargins(left, top, right, bottom)


    .. js:function:: SetOrientation(orient)


    .. js:function:: SetPadding(left, top, right, bottom)

        Устанавливает внутренние отступы компонента в процентах

        .. code-block:: js
            
            lay.SetPadding(0.1, 0.1, 0.1, 0.1);


    .. js:function:: SetPosition(left, top, width, height)

    
    .. js:function:: SetScale(x, y)

    .. js:function:: SetSize(width, height)


    .. js:function:: SetTouchable(touchable)


    .. js:function:: SetVisibility(visibility)

        Устанавливает видимость компонента 'Hide', 'Show', 'Gone'

        .. code-block:: js            
            
            lay.SetVisibility('Hide');
            lay.SetVisibility('Show');


    
        
