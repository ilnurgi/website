.. py:module:: tkinter

Canvas
======

Виджет, холст

.. py:class:: Canvas(**kwargs)

    Наследник :py:class:`Widget`, :py:class:`XView`, :py:class:`YView`

    * master - родительский виджет
    * cnf - словарь
    * closeenough -
    * confine - булево, выключить скрол холста за пределы региона
    * height - :py:class:`int`, высота виджета
    * insertbackground -
    * insertborderwidth -
    * insertofftime -
    * insertontime -
    * insertwidth -
    * offset -
    * scrollregion - кортеж (w, n, e, s), что-то там с покруткой
    * selectbackground -
    * selectborderwidth -
    * selectforeground -
    * state -
    * width - :py:class:`int`, ширина виджета
    * xscrollcommand - обработчик горизонтальной прокрутки
    * xscrollincrement - величина горизонтальной прокрутки
    * yscrollcommand - обработчик вертикальной прокрутки
    * yscrollincrement - величина вертикальной прокрутки

    .. code-block:: py

        canvas = Canvas(master)

        # биндим проведение мышкой
        canvas.bind("<B1-Motion>", lambda event: pass)
        canvas.bind("<Double-1>", lambda event: pass)

    .. code-block:: py

        canvas = Canvas(
            master,
            width=300,
            height=300,
            bg="white",
            relief=SUNKEN,
        )

    .. code-block:: py

        # холст с прокруткой

        canv = Canvas(master)
        canv.config(width=300, height=200)
        canv.config(scrollregion=(0,0,300, 1000))
        canv.config(highlightthickness=0)

        sbar = Scrollbar(master)
        sbar.config(command=canv.yview)

        canv.config(yscrollcommand=sbar.set)


    .. py:method:: addtag(tag, method, *args)

        Добавляет тег элементам

        * `tag` - тег
        * `method` - способ добавления
            * above - выше
            * all - всем
            * below - ниже
            * closest - ближе
            * enclosed -
            * overlaping
            * withtag


    .. py:method:: addtag_above(newtag, tagOrId)

        Добавляет новый тег элементу


    .. py:method:: addtag_all(newtag)

        Добавляет новый тег всем элементам


    .. py:method:: addtag_below(newtag, tagOrId)

        Добавляет новый тег элементу


    .. py:method:: addtag_closest(newtag, x, y, halo=None, start=None)

        Добавляет новый тег элементу, который ближе к указанной точке


    .. py:method:: addtag_enclosed(newtag, x1, y1, x2, y2)

        Добавляет тег элементам, в указанной области


    .. py:method:: addtag_overlapping(self, newtag, x1, y1, x2, y2)

        Добавляет тег элементам, перекрывающих указанную область


    .. py:method:: addtag_withtag(newtag, tagOrId)

        Добавляет тег элементу по его идентификатору или тегу

        .. code-block:: py

            canvas.addtag_withtag("three", "one")


    .. py:method:: bbox(*args)

        Возвращает координаты прямоугльника, в которой находятся указанные объекты холста

        .. code-block:: py

            head = canvas.find_withtag("head")
            x1, y1, x2, y2 = canvas.bbox(head)


    .. py:method:: canvasx(screenx, gridspacing=None)

        Возвращает координату на канвасе по координате экрана


    .. py:method:: canvasy(screeny, gridspacing=None)

        Возвращает координату на канвасе по координате экрана


    .. py:method:: coords(*args)

        Возвращает область, в которой находятся указанные объекты


    .. py:method:: create_arc(*args, **kwargs)

        Рисует круг, вписанную в прямоугольник, и возвращает его идентификатор

        * `activedash`
        * `activefill`
        * `activeoutline`
        * `activeoutlinestipple`
        * `activestipple`
        * `activewidth`
        * `dash`
        * `dashoffset`
        * `disableddash`
        * `disabledfill`
        * `disabledoutline`
        * `disabledoutlinestipple`
        * `disabledstipple`
        * `disabledwidth`
        * `extent` - число, угол, величина рисуемой окружности
        * `fill` - строка, цвет заполнения
        * `offset`
        * `outline` - цвет контура
        * `outlineoffset`
        * `outlinestipple`
        * `start` - число, угол, начало рисования
        * `state`
        * `stipple`
        * `style`
        * `tag` - название объекта
        * `tags`
        * `width` - ширина контура


    .. py:method:: create_bitmap(*args, **kwargs)

        * `activebackground` -
        * `activebitmap` -
        * `activeforeground` -
        * `anchor` -
        * `background` -
        * `bitmap` -
        * `disabledbackground` -
        * `disabledbitmap` -
        * `disabledforeground` -
        * `foreground` -
        * `state` -
        * `tags` -


    .. py:method:: create_image(h, w, **kwargs)

        Рисует изображение и возвращает его идентификатор

        * `activeimage`
        * `anchor` - NW
        * `disabledimage`
        * `image` - :py:class:`Image`, рисунок
        * `state`
        * `tags`

        .. code-block:: py

            image_id = canvas.create_image(
                height,
                width,
                image=PhotoImage(),
                anchor=NW,
            )


    .. py:method:: create_line(x1, y1, x2, y2, ..., x-n, y-n, **kwargs)

        Рисует линию и возвращает его идентификатор

        * `activedash`
        * `activefill`
        * `activestipple`
        * `activewidth`
        * `arrow`
        * `arrowshape`
        * `capstyle`
        * `dash` - для рисования штрихами, длина пунктира и пропуска, например (4, 2)
        * `dashoffset`
        * `disableddash`
        * `disabledfill`
        * `disabledstipple`
        * `disabledwidth`
        * `fill` - цвет линии
        * `joinstyle`
        * `offset`
        * `smooth`
        * `splinesteps`
        * `state`
        * `stipple`
        * `tags` - задает тег для элемента
        * `width` - ширина линии

        .. code-block:: py

            line_id = canvas.create_line(
                x1,
                y1,
                x2,
                y2,
                tags="uno",
                fill="green",
                width=10,
            )


    .. py:method:: create_oval(x1, y1, x2, y2, **kwargs)

        Рисует овал и возвращает идентификатор

        * `activedash`
        * `activefill`
        * `activeoutline`
        * `activeoutlinestipple`
        * `activestipple`
        * `activewidth`
        * `dash`
        * `dashoffset`
        * `disableddash`
        * `disabledfill`
        * `disabledoutline`
        * `disabledoutlinestipple`
        * `disabledstipple`
        * `disabledwidth`
        * `fill` - цвет заливки
        * `offset`
        * `outline` - цвет контура
        * `outlineoffset`
        * `outlinestipple`
        * `state`
        * `stipple`
        * `tags`
        * `width` - ширина границы

        .. code-block:: py

            oval_id = canvas.create_oval(
                x1,
                y1,
                x2,
                y2,
                fill="red",
                width=2,
            )


    .. py:method:: create_polygon(x1, y1, x2, y2, ..., x-n, y-n, **kwargs)

        Рисуем замкнутый контур и возвращает его идентификатор

        * `activedash`
        * `activefill`
        * `activeoutline`
        * `activeoutlinestipple`
        * `activestipple`
        * `activewidth`
        * `dash`
        * `dashoffset`
        * `disableddash`
        * `disabledfill`
        * `disabledoutline`
        * `disabledoutlinestipple`
        * `disabledstipple`
        * `disabledwidth`
        * `fill` - цвет заливки
        * `joinstyle`
        * `offset`
        * `outline` - цвет линии
        * `outlineoffset`
        * `outlinestipple`
        * `points` - список точек
        * `smooth`
        * `splinesteps`
        * `state`
        * `stipple`
        * `tags`
        * `width` - высота линии


    .. py:method:: create_rectangle(x1, y1, x2, y2, **kwargs)

        Рисует многоугольник и возвращает его идентификатор

        * `activedash`
        * `activefill`
        * `activeoutline`
        * `activeoutlinestipple`
        * `activestipple`
        * `activewidth`
        * `dash`
        * `dashoffset`
        * `disableddash`
        * `disabledfill`
        * `disabledoutline`
        * `disabledoutlinestipple`
        * `disabledstipple`
        * `disabledwidth`
        * `fill` - цвет заливки
        * `offset`
        * `outline` - цвет контурв
        * `outlineoffset`
        * `outlinestipple`
        * `state`
        * `stipple`
        * `tags`
        * `width` - ширина границ

        .. code-block:: py

            rectangle_id = canvas.create_rectangle(
                x1,
                y1,
                x2,
                y2,
                width=5,
                fill="red",
            )


    .. py:method:: create_text(x, y, **kwargs)

        Рисует текст и возвращает его идентификатор

        * `activefill`
        * `activestipple`
        * `anchor` - W
        * `disabledfill`
        * `disabledstipple`
        * `fill`
        * `font` - Purisa
        * `justify`
        * `offset`
        * `state`
        * `stipple`
        * `tags`
        * `text` - текст
        * `width`

        .. code-block:: py

            text_id = canvas.create_text(
                x,
                y,
                text="Some text",
            )


    .. py:method:: create_window(x, y, window)

        Рисует виджет на холсте и возвращает id

        * `anchor`
        * `height`
        * `state`
        * `tags`
        * `width`
        * `window`

        .. code-block:: py

            canvas.create_window(x, y, widget)


    .. py:method:: dchars(item, from, to=None)

        Удаляет текст из элемента


    .. py:method:: delete(**kwargs)

        Удаляет объекты с холста

        .. code-block:: py

            apple = canvas.find_withtag('apple')
            canvas.delete(apple[0])


    .. py:method:: dtag(item, tag=None)


    .. py:method:: find_above(item)
    .. py:method:: find_all()
    .. py:method:: find_below(item)
    .. py:method:: find_closest(x, y, halo=None, start=None)
    .. py:method:: find_enclosed(x1, y1, x2, y2)
    .. py:method:: find_overlapping(x1, y1, x2, y2)

        Возвращает все объекты, которые находятся в указанной области


    .. py:method:: find_withtag(tagOrId)

        Возвращает список объектов холста, соответсвующих указанному тегу или идентификатору

        .. code-block:: py

            canvas.find_withtag('one')
            # (1, )


    .. py:method:: focus(item=None)
    .. py:method:: gettags(*args)

        Возвращает теги элементов

        .. code-block:: py

            canvas.gettags(item)
            # ('one', 'two', 'three')


    .. py:method:: icursor(item, index)


    .. py:method:: index(item, index)


    .. py:method:: insert(item, index, text)

        Добавляет текст в редактируемый элемент


    .. py:method:: itemconfig(id, **kwargs)
    .. py:method:: itemconfigure(id, **kwargs)

        Конфигурирует объект рисования

        * `tags` - изменяет теги объекта

        .. code-block:: py

            canvas.itemconfig(item, tags=("one", "two"))


    .. py:method:: itemcget(tagOrId, option)

        Возвращает значение свойства элемента


    .. py:method:: lift()
    .. py:method:: tkraise()
    .. py:method:: tag_raise()

        Поднимает объект относительно других


    .. py:method:: lower()
    .. py:method:: tag_lower()

        Опускает объект относитльно других


    .. py:method:: move(tag, x, y)

        Сдвигает объекты


    .. py:method:: postscript(*args)


    .. py:method:: scale(tagOrId, xscale, yscale, xoffset, yoffset)

        Изменяет размер элемента


    .. py:method:: scan_dragto(x, y, gain=10)


    .. py:method:: scan_mark(x, y)


    .. py:method:: select_adjust(tagOrId, index)


    .. py:method:: select_clear()


    .. py:method:: select_from(tagOrId, index)


    .. py:method:: select_item()


    .. py:method:: select_to(tagOrId, index)


    .. py:method:: tag_bind(tagOrId, sequence=None, func=None, add=None)

        Связываем обработчик с событиями элемента

        .. code-block:: py

            canvas.tag_bind(obj_id, "<Double-1>", lambda event: pass)


    .. py:method:: tag_unbind(tagOrId, sequence, funcid=None)


    .. py:method:: type(tagOrId)

