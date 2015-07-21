.. py:module:: graphics

graphics
========

Данный модуль обеспечивает доступ к объектам и функциям для работы с изображениями. 

.. py:method:: screenshot() 
    
    Возвращает объект :py:class:`Image`, содержащий изображения экрана. Отмечу, если программа, с которой снимают скриншот, использует вывод через OpenGL ES 3D, то изображение получается с искажениями.

Image() 
-------

.. py:class:: Image() 

.. py:staticmethod:: Image.new(size [, mode='RGB16']) 
    
    :param size: размер нового изображения
    :type size: tuple(x, y)
    :param mode: цветовая глубина

        * '1' - черно-белое изображения (1 бит на пиксель);
        * 'L' - 256 оттенков цвета (8 бит на пиксель);
        * 'RGB12' - 4096 оттенков цвета (12 бит на пиксель);
        * 'RGB16' - 65536 оттенков цвета (16 бит на пиксель);
        * 'RGB' - 16.7 миллионов оттенков цвета (24 бит на пиксель).

    Возвращает объект :py:class:`Image`

.. py:staticmethod:: Image.open(filename) 

    :param filename: путь к изображению
    
    Открывает графический файл (форматы JPG и PNG) и возвращает в виде объекта :py:class:`Image`. 

.. py:staticmethod:: Image.inspect(filename) 

    :param filename: путь к изображению

    Возвращает словарь, элемент которого с ключом «size» содержит кортеж - длина и высота изображения

.. py:method:: Image.load(filename [, callback=None]) 
    
    Открывает изображение и заменяет им существующее изображение (их размеры должны быть одинаковы). 

.. py:method:: Image.resize(newsize [, callback=None, keepaspect=0 ]) 

    :param newsize: новый размер
    :type newsize: tuple(x, y)
    :param calback: функция обработчик
    :param keepaspect: 0|1 сохранять пропорции
    
    Изменяет размер изображения

.. py:method:: Image.transpose(direction [, callback=None]) 

    :param direction: тип операции
        
        * graphics.FLIP_LEFT_RIGHT - переворачивает слева направо;
        * graphics.FLIP_TOP_BOTTOM - переворачивает снизу вверх;
        * graphics.ROTATE_90 - поворачивает на 90 градусов по часовой стрелке;
        * graphics.ROTATE_180 - поворачивает на 180 градусов;
        * graphics.ROTATE_270 - поворачивает на 270 градусов.

    Возвращает новое изображение, полученное на основе оригинала к которому была применена операция.

.. py:method:: Image.save(filename [,callback=None, format=None, quality=75, bpp=24, compression='default' ]) 

    :param filename: путь к файлу
    :param calback: обработчик
    :param format: формат изображения
    :type format: 'JPG', 'PNG'
    :param qualite: качество (0...100) hpeg
    :param bpp: битность (1, 8, 24) png
    :param compression: сжатие
        * 'default' - по умолчанию (компромисс между скоростью и качеством сжатия);
        * 'best' - максимальное сжатие, но медленная скорость;
        * 'fast' - быстро, но компрессия слабая;
        * 'no' - без сжатия (файл получается большим, но зато абсолютно без артефактов присущих формату JPG).

    Сохраняет изображение Image в графическом файле filename.

.. py:method:: Image.stop() 
    
    Указывает прервать выполнение асинхронных функций :py:meth:`resize`, :py:meth:`transpose`, :py:meth:`load` и :py:meth:`save`. Дело вот в чем, если при вызове этих функций не указан аргумент callback, то они становятся синхронными. Т.е. они прерывают выполнение программы до тех пор, пока операция не будет завершена (загрузка большого файла, например, может быть длительной по времени, и программа даже может «подвиснуть»). 
    А вот если мы указали callback (имя функции), то :py:meth:`resize`, :py:meth:`transpose`, :py:meth:`load` и :py:meth:`save` становятся асинхронными. Т.е. они не прерывают выполнение программы, и работа идет дальше, но после завершения процессов (например, сохранение) сразу вызывается функция callback. Так вот stop и указывать прервать все эти процессы досрочно. 

.. py:attribute:: Image.size 
    
    Кортеж, первый элемент которого указывает длину изображения, второй - его ширину. 

.. py:attribute:: Image.twipsize 
    
    Кортеж, первый элемент которого указывает длину изображения, второй - его ширину в твипсах

Методы рисования примитивов
---------------------------

При рисовании цвета могут указываться как число в шестнадцатеричном представлении (0xRRGGBB), так и как кортеж из 3 чисел, каждый из которых отвечает за одну составляющую цвета - (red, green, blue). Диапазон чисел от 0 до 255. 

.. py:method:: Image.arc(rect, start, end [, outline = 0xffffff [, width = 1]]) 

    :param rect: вписываемый прямоугольник
    :type rect: (x1, y1, x2, y2)
    :param start: начальный угол сектора
    :param end: конечный угол сектора
    :param outline: цвет контура
    :param width: размер контура
    
    Рисует дугу вырезанную из эллипса, вписанного в прямоугольник с углами в точках x1, y1 и x2, y2, имеющего контур шириной width и цветом outline. Аргументы start и end указывают начальный и конечный угол сектора. 

.. py:method:: Image.blit(image [, target = (0,0) [, source = ((0,0), image.size) [, mask = None [, scale = 0 ]]]]) 

    :param image: копируемое изображение
    :param target: смещение относительно (0, 0)
    :param source: определенная область источника
    :param mask: маска для копируемого изображения, черно-белое изображение, размер которого совпадает с размером копируемого участка и указывает, какие пиксели выводить, а какие нет;
    :param scale: масштабирование (использование этого атрибута замедляет выполнение операции).
    
    Копирует изображение на оригинальное изображение

.. py:method:: Image.clear([ color = 0xffffff]) 
    
    Заполняет изображение определенным цветом


.. py:method:: Image.ellipse(rect [, outline = 0xffffff [, fill = 0[, width = 1]]]) 
    
    :param rect: вписываемый прямоугольник
    :type rect: (x1, y1, x2, y2)    
    :param outline: цвет контура
    :param fill: цвет заливки
    :param width: размер контура

    Рисует эллипс, вписанный в прямоугольник.

.. py:method:: Image.line(pos [, outline = 0xffffff [, width = 1]]) 
    
    :param pos: координаты
    :type pos: (x1, y1, x2, y2)    
    :param outline: цвет контура
    :param width: размер контура

    Рисует линию

.. py:method:: Image.measure_text(text [, font=None [, maxwidth = -1[, maxadvance = -1 ]]]) 
    
    :param text: рисуемый текст
    :param font: шрифт текста
    :param maxwidth: максимальная ширина изображения
    :param maxadvance: максимальная высота курсора. 

    Определяет тот размер изображения, в котором уместится нарисованный шрифтом текст. Возвращает кортеж из трех элементов: 
        * (topleft - x, topleft - y, bottomright - x, bottomright - y) - прямоугольник, ограничивающий текст;
        * число пикселей для графического курсора;
        * количество символов текста, которое вписывается в полученный прямоугольник.

.. py:method:: Image.pieslice(rect, start, end [, outline = 0xffffff [, fill = 0 [, width = 1]]]) 
    
    :param rect: вписываемый прямоугольник
    :type rect: (x1, y1, x2, y2)   
    :param start: начальный угол сектора. Углы отчитываются от правой полуоси и измеряются в радианах (0 - правый, pi/2 -верх, pi - левый, 2*pi/3 - низ)
    :param end: конечный угол сектора 
    :param outline: цвет контура
    :param fill: цвет заливки
    :param width: размер контура

    Рисует сектор вырезанной из эллипса, вписанного в прямоугольник

.. py:method:: Image.point(pos [, outline = 0xffffff [, width = 1]]) 
    
    :param pos: вписываемый прямоугольник
    :type pos: (x1, y1, x2, y2)    
    :param outline: цвет контура    
    :param width: размер контура

    Рисует точку.

.. py:method:: Image.polygon(rect [, outline = 0xffffff [, fill = 0 [, width = 1]]]) 
    
    :param rect: координаты вершин
    :type rect: (x1, y1, x2, y2,..., xN, yN)    
    :param outline: цвет контура
    :param fill: цвет заливки
    :param width: размер контура

    Рисует многоугольник

.. py:method:: Image.rectangle(rect [, outline = 0xffffff [, fill = 0[, width = 1]]]) 
    
    :param rect: координаты вершин
    :type rect: (x1, y1, x2, y2)
    :param outline: цвет контура
    :param fill: цвет заливки
    :param width: размер контура

    Рисует прямоугольник с противоположными углами в точках

.. py:method:: Image.text(pos, text [, fill = 0xffffff [, font = None]]) 
    
    :param pos: ккординаты вставки текста
    :type pos: (x1, y1)    
    :param text: текст
    :type text: unicode
    :param fill: цвет текста
    :param font: шрифт, unicode строка ('normal', 'dense', 'title', 'symbol', 'legend', 'annotation') или кортеж (font, size[, style])

        * font - имя шрифта, None - по умолчанию
        * size - размер шрифта, None - по умолчанию
        * style - стиль шрифта

            * graphics.FONT_BOLD(жирный);
            * graphics.FONT_ITALIC(наклоненный);
            * graphics.FONT_SUBSCRIPT(подстрочный);
            * graphics.FONT_SUPERSCRIPT(надстрочный);
            * graphics.FONT_ANTIALIAS (со сглаживанием)
            * graphics.FONT_NO_ANTIALIAS(без сглаживания);