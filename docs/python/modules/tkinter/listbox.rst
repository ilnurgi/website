Listbox - виджет, список
========================


.. py:class:: Listbox(**kwargs)

    Виджет список

    Наследник :py:class:`Widget`, :py:class:`XView`, :py:class:`YView`

    * `exportselection` -
    * `listvariable` -
    * `selectbackground` - строка, цвет фона выбранного элемента
    * `selectborderwidth` - строка, ширина границы выбранного элемента
    * `selectforeground` - строка, цвет текста выбранного элемента
    * `selectmode` - константа :ref:`const_listbox_select`, выбор элементов списка

        * SINGLE - один элемент
        * BROWSE - один элемент с возможностью перетаскивания
        * MULTIPLE - множественный выбор
        * EXTENDED - множественный выбор, с возможностью добавления

    * `setgrid` -
    * `width` -
    * `xscrollcommand` - виджет горизонтальной прокрутки
    * `yscrollcommand` - виджет вертикальнной прокрутки

    .. code-block:: py

        # со скроллом
        scrollbar = Scrollbar(master)

        listbox = Listbox(
            master,
            xscrollcommand=scrollbar.set,
            selectmode=EXTENDED,
        )

        scrollbar.config(command=listbox.xview)


    .. py:method:: activate(index)

        Активирует элемент по указанному индексу


    .. py:method:: curselection()

        Возвращает кортеж, выбранных значений


    .. py:method:: delete(first, last=None)

        Удаляет элементы из виджета

        .. code-block:: py

            # удалить все эелементы из виджета
            listbox.delete(0, END)


    .. py:method:: get(first, last=None)

        Возвращает элемент по позиции или элементы промежутка


    .. py:method:: index(i)

        Возвращает индекс индекса


    .. py:method:: insert(pos, *elements)

        Добавляет в виджет элементы


    .. py:method:: nearest(y)

        Возвращает индекс видимого элемента, ближайшего к указанной координает


    .. py:method:: see(index)

        Прокручивает виджет до указанного индекса


    .. py:method:: size()

        Возвращает количесвто элементов в виджете

