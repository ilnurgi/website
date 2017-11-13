.. py:module:: tkinter

Button
======

Виджет, кнопка


.. py:class:: Button(**kwargs)

     Наследник :py:class:`Widget`

    * background - :py:class:`str`, цвет фона
    * bg - :py:class:`str`, цвет фона
    * command - ссылка на функцию обработчика
    * compound
    * default
    * fg - :py:class:`str`, цвет текста
    * height - :py:class:`int`, высота виджета, количесвто строк - для обычной кнопки, пиксели - для кнопки картинки
    * image - кнопка-картинка
    * overrelief
    * state - константа :ref:`const_state`
    * text - :py:class:`str`, текст надписи на кнопке
    * width - :py:class:`str`, ширина виджета, количесвто символов - для обычной кнопки, пиксели - для кнопки картинки

    .. code-block:: py

        button = Button(
            master,
            text="some text",
            command=lambda: pass,
            image=PhotoImage(),
        )

    .. code-block:: py

        button = Button(master)
        button["text"] = "Some text"
        button.bind("<Button-1>", lambda event: pass)


    .. py:method:: bind(event_name, callback)

        Создает обработчик события для виджета

        * event_name - :py:class:`str`, название события

            * <Button-1> - двойной клик на элементе

            * <<ListboxSelect>> - клик на элементе

        * callback - функция обработчик

        .. code-block:: py

            button.bind('<Button-1>', lambda event: pass)
            

    .. py:method:: flash()

        Вспышка кнопки, чередование активной и нормальной цветов.


    .. py:method:: invoke()

        Возвращает результат работы обработчика кнопки

    .. py:method:: pack(**kwargs)

        Один из менеджеров расположения, распологает виджеты один за другим.

        * `after` - :py:class:`Widget`, расположить виджет после указанного
        * `anchor` - константа :ref:`const_anchor_sticky`
        * `before` - :py:class:`Widget`, расположить виджет перед указанным
        * `cnf` - словарь
        * `expand` - константа :ref:`const_bool`, растягивать виджет при изменении окна
        * `fill` - константа :ref:`const_fill` родителя
            * BOTH - По всем направлениям
            * None - Без заполнения
            * X - По горизонтали
            * Y - По верикали
        * `in` - :py:class:`Widget`
        * `in_` - :py:class:`Widget`
        * `ipadx` - отступ виджета по горизонтали
        * `ipady` - отступ виджета по вертикали
        * `padx` - внутренний отступ виджета по горизонтали
        * `pady` - внутренний отступ виджета по вертикали
        * `side` - константа :ref:`const_side` на родителе

            * :py:attr:`tkinter.LEFT`
            * :py:attr:`tkinter.RIGHT`


        .. code-block:: py

            button.pack(side=LEFT)