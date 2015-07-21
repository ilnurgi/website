.. py:module:: txtfield

txtfield
========

Модуль для создания текстовых полей. 

автор: watt

.. py:method:: LoadFont(filename) 
    
    Загружает свой шрифт в систему, возвращает идентификатор шрифта. 
    
    .. note:: если возвращаемое значение == 0, шрифт не будет удален и останется висеть в системе до следующей перезагрузки. 
    
    .. note:: НЕ используйте шрифты с внутреними именами равными системным (шрифт будет "виден" из любой программы)
    
    >>> txtfield.LoadFont(u'e:\\myfont.gdr')

.. py:method:: RemoveFont(id) 
    
    :param id: идентификатор шрифта из функции ;py:meth:`LoadFont()`
    
    Выгружает шрифт из системы 
    
.. py:method:: ShadowVector(x,y) 
    
    Установливает вектор тени.
    
    >>> txtfield.ShadowVector(-1,3)

.. py:class:: New((rect) [,strlimit=0, txtlimit=0, cornertype= ECornerSquare, cornerflag=None, editorflag=None, picalign=EPicBaseLine, callback=None]) 
    
    :param rect: (x1, y1, x2, y2) координаты окна
    :param strlimit: допустимое количество строк
    :param txtlimit: максимальное количество символов
    :param cornertype: скругление углов
        
        * txtfield.ECornerSquare
        * txtfield.ECorner1
        * txtfield.ECorner2
        * txtfield.ECorner5

    :param cornerflag: какие углы не скруглять
        
        * txtfield.ENotTL - верхний-левый
        * txtfield.ENotTR - верхний-правый
        * txtfield.ENotBL - нижний-левый
        * txtfield.ENotBR - нижний-правый

    :param editorflag:

        * txtfield.EDisplayOnly - не реагирует на действия пользователя
        * txtfield.EAlwaysShowSelection - при смене фокуса выделение не снимается
        * txtfield.EReadOnly - только для чтения
        * txtfield.ENoLineBreaks - не допускает переноса строки
        * txtfield.EDisableCursor - скрывает курсор
        * txtfield.picalign - выравнивание картинки относительно текста:
        * txtfield.EPicBaseLine - по линии текста
        * txtfield.EPicBottom - по низу
        * txtfield.EPicCentered - по центру
        * txtfield.EPicTop - по верху

    :param callback: обработчик, в которую передается -1 после изменения, 0-навигация, и сканкод клавиши после EEventKeyDown
    
    Данный класс создает текстовое поле.


    >>> txt1 = txtfield.New(
            (20,120,156,200),
            cornertype = txtfield.ECorner2,
            cornerflag = txtfield.ENotTL | txtfield.ENotBR, 
            editorflag = txtfield.EAlwaysShowSelection | txtfield.EReadOnly)
    >>> txt2 = txtfield.New((20,120,156,200))

.. py:method:: New._set(c) 
    
    Вроде устанавливает скорость прокрутки 

.. py:method:: New.add(text [,select=0]) 

    :param text: тектс
    :param select: 0|1 вставить с выделение
    
    Добавляет текст с текущей позиции курсора

.. py:method:: New.align(Alignment) 
    
    Выравнивание текста 

        * txtfield.ELeftAlign - по левому краю
        * txtfield.ETopAlign - по верху
        * txtfield.ECenterAlign - по центру
        * txtfield.ERightAlign - по правому краю
        * txtfield.EBottomAlign - по низу
        * txtfield.EJustifiedAlign
        * txtfield.EUnspecifiedAlign - без выравнивания

.. py:method:: New.bgcolor(color) 
    
    Установить цвет фона в hex формате
    
    >>> txt1.bgcolor(0x88bb33)

.. py:method:: New.clear([pos,len]) 
    
    Очистить текст

.. py:method:: New.clipboard(True|False) 
    
    Если True - вставить из буфера, если False - скопировать в буфер выделенный текст 

.. py:method:: New.focus(True|False) 
    
    Установить-снять фокус окна 

.. py:method:: New.get() 
    
    Получить текст окна, возвращает юникод строку. 

.. py:method:: New.info() 
    
    Возвращает кортеж: (len,position,isvisible,isfocus,piccount,wordcount,strcount,linepos)
        
        * len - длинну текста
        * position - текущую позицию курсора
        * isvisible - True-если окно видно или False если нет
        * isfocus - True-если окно в фокусе или False если нет
        * piccount - количество картинок
        * wordcount - количество слов
        * strcount - количество строк
        * linepos - номер текущей строки

.. py:method:: New.input_mode(mode) 

    :param mode: 

        * txtfield.NumericInputMode=2, 
        * txtfield.TextInputMode=1
    
    Установить режим ввода

    >>> txt1.input_mode(txtfield.NumericInputMode)
    >>> txt2.input_mode(2)

.. py:method:: New.move(MovementType [,pix=20]) 
    
    :param MovementType:

        * txtfield.EFLeft - слево на право
        * txtfield.EFRight - справо на лево
        * txtfield.EFLineUp - текст на строку вниз
        * txtfield.EFLineDown - текст на строку вверх
        * txtfield.EFPageUp - страница вверх
        * txtfield.EFPageDown - страница вниз

    :param pix: на сколько пикселей перемещать текст при горизонтальной прокрутке. 

    Перемещение текста

.. py:method:: New.set_border(width,color) 
    
    :param width: ширина
    :param color: цвет
    :type color: hex

    Установить бордюр

.. py:method:: New.set_interval(twips) 
    
    Установить расстояние между строками

.. py:method:: New.set_margin(LeftMargin,RightMargin) 
    
    Установить левый и правый отступ 

.. py:method:: New.select(start,end) 
    
    Выделить текст

.. py:method:: New.setcursor(pos) 
    
    Установить курсор в позицию 

.. py:method:: New.setimg(img, pos, rect) 

    :param img: изображение
    :type img: :py:class:`graphics.Image`
    :param pos: позиция установки
    :param rect: размер изображения
    :type rect: (x, y)
    
    Вставляет картинку в поле

.. py:method:: New.setpos(x,y) 
    
    Установить новую позицию окна 

.. py:method:: New.setsize(x,y) 
    
    Установить новый размер окна 

.. py:method:: New.shadow(size) 
    
    Добавить тень к окну в размер size 

.. py:method:: New.textstyle(name[,size,color,style=u"Normal"]) 
    
    :param name: название шрифта
    :param size: размер шрифта
    :param color: цвет шрифта
    :type color: hex
    :param style: стиль шрифта, (normal, bold, italic, italic-bold)
    
    >>> txt1.textstyle(name=u'Nokia Sans S60', size=130, color=0x119922, style=u'bold')
    >>> txt2.textstyle(u'Nokia Sans S60', 130, 0x119922, u'bold')

.. py:method:: New.visible(True|False) 
    
    Показать-спрятать окно 

.. py:method:: New.z_index(index) 
    
    Переместить поле наверх или вниз(в зависимости от индекса других полей), значение index: 0-100
