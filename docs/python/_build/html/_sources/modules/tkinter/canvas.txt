Canvas
======

.. py:class:: Canvas(widget, **kwargs)

    Виджет, холст

    .. py:method:: create_arc(x1, y1, x2, y2, **kwargs)

        Рисует круг, вписанную в прямоугольник, и возвращает id

        :param start: угол, начало рисования
        :param extent: угол, величина рисуемой окружности
        :param str fill: цвет заполнения
        :param str outline: цвет контура
        :param int width: ширина контура
        :param str tag: название объекта 

    .. py:method:: creale_line(x1, y1, x2, y2, ....)

        русет линии, и возвращает id

    .. py:method:: create_oval(x1, y1, x2, y2)

        рисует овал, и возвращает id

    .. py:method:: create_polygon(x1, y1, x2, y2, ...)

        рисуем ассиметричный многоугольник, и возвращает id

    .. py:method:: create_rectangle(x1, y1, x2, y2)

        рисует многоугольник, и возвращает id

    .. py:method:: create_image(h, w, img)

        рисует изображение, и возвращает id

        :param int h: высота
        :param int w: ширина
        :param img: объект рисунок
        :type img: :py:class:`PhotoImage`

    .. py:method:: create_window(x, y, window)

        Рисует окно, и возвращает id

    .. py:method:: itemconfig(id, **kwargs)

        Конфигурирует объект рисования

    .. py:method:: delete(id)

        Удаляет объект из холста

    .. py:method:: tkraise()

        Поднимает объект относительно других

    .. py:method:: lower()

        Опускает объект относитльно других

    .. py:method:: addtag_withttag(tag, id)

        Добавляет тег к объекту

    .. py:method:: move(tag, x, y)

        Сдвигает объекты
