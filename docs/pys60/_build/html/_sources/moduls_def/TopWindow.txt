.. py:module:: TopWindow

TopWindow
=================================

.. py:class:: TopWindow

    >>> window = TopWindow.TopWindow()

    .. py:attribute:: position 

        Координаты окна отображения на экране
    
        >>> window.position = (10, 20)

    .. py:attribute:: size 
        
        Размеры окна
        
        >>> window.size = (100, 200)
    
    .. py:attribute:: images 
        
        Список кортежей [(graphics.Image, position), ] изображений на окне.

        >>> images.images = [(image1,(x1,y1)), (image2,(x1,y1,x2,y2)), (image3,(50,50,100,100))]
    
    .. py:attribute:: shadow 
        
        Создает тень у окна 

    .. py:attribute:: corner_type 
        
        Типы углов окна
    
            * square
            * corner1
            * corner2
            * corner3
            * corner5
    
    .. py:attribute:: maximum_size 
        
        Возвращает кортеж (x, y) максимально возможный размер окна системы. 

    .. py:attribute:: background_color 
        
        Цвет фона окна 

    .. py:attribute:: visible 
        
        Видимый

    .. py:method:: show() 
    
        Отображает окно 

        >>> window.show()

    .. py:method:: hide() 
    
        Скрывает окно 

        >>> window.hide()

    .. py:method:: add_image(image, pos) 

        :param image: изображение
        :type image: graphics.Image
        :param pos: координаты, (x1, y1[, x2, y2])
        :type pos: tuple
        
        Вставляет в окно изображение.

        >>> window.add_image(image, (10,20))
        >>> window.add_image(image, (10,20,20,30))
    
    .. py:method:: remove_image(image[,position ]) 
        
        :param image: изображение
        :type image: graphics.Image
        :param pos: координаты, (x1, y1[, x2, y2])
        :type pos: tuple

        Удаляем изображение из окна.
    
        >>> window.remove_image(image)
        >>> window.remove_image(image, (10,10))
        >>> window.remove_image(image, (10,10,20,20))
    
