.. py:module:: tkinter

Text - виджет, поле ввода текста
================================

.. py:class:: Text(**kwargs)

    Виджет, многострочное текстовое поле.

    Наследник:

        * :py:class:`tkinter.Widget`
        * :py:class:`tkinter.XView`
        * :py:class:`tkinter.YView`

    * `autoseparators` -
    * `exportselection` -
    * `height` -
    * `insertbackground` -
    * `insertborderwidth` -
    * `insertofftime` -
    * `insertontime` -
    * `insertwidth` -
    * `maxundo` -
    * `selectbackground` -
    * `selectborderwidth` -
    * `selectforeground` -
    * `setgrid` -
    * `spacing1` -
    * `spacing2` -
    * `spacing3` -
    * `state` -
    * `tabs` -
    * `undo` -
    * `xscrollcommand` -
    * `yscrollcommand` -
    * `width` -
    * `wrap` - константа :ref:`const_wrap`

    .. code-block:: py

        # со скроллом
        scrollbar = Scrollbar(master)

        text = Text(
            master,
            yscrollcommand=scrollbar.set,
        )

        scrollbar.config(command=text.yview)


    .. py:method:: get(index1, index2=None)

        Возвращает символы в указанном промежутке

        .. code-block:: py

            text.get('1.0', 'END')


    .. py:method:: delete(index1, index2)

        Удаляет символы в указанном промежутке

        .. code-block:: py

            text.delete('1.0', 'END')


    .. py:method:: index(index)
    .. py:method:: index(mark)

        Возвращает индекс индекса или индекс указанной метки


    .. py:method:: insert(index, chars, *args)

        Вставляет символы от указаннйой позиции

        .. code-block:: py

            text.insert(1.0, 'strings')
            text.insert(INSERT, "Hello.....")
            text.insert(END, "Bye Bye.....")


    .. py:method:: mark_gravity(markName, direction=None)

        Задает вес метке


    .. py:method:: mark_names()

        Возвращает список всех меток


    .. py:method:: mark_set(markName, index)

        Устанавливает метку

        .. code-block:: py

            t.mark_set('first', '2.5')


    .. py:method:: mark_unset(*markNames)

        Удаляет метки


    .. py:method:: see(index)

        Прокручивает виджет до указанной позиции


    .. py:method:: tag_add(tagName, index1, *args)

        Добавляет тег в текст

        .. code-block:: py

            t.tag_add('tag', SEL_FIRST, SEL_LAST)
            text.tag_add("here", "1.0", "1.4")


    .. py:method:: tag_config(tagName, cnf=None, **kwargs)
    .. py:method:: tag_configure(tagName, cnf=None, **kwargs)

        Конфигурирует тег

        .. code-block:: py

            t.tag_config('tag', background='black', foregraund='red', font=('times', 14, 'italic'))


    .. py:method:: tag_delete(*tagNames)

        Удаляет теги


    .. py:method:: tag_remove(tagName, index1, index2=None)

        Удаляет тег из указанного промежутка


    .. py:method:: see(pos)

        Прокручивает текстовое поле до позиции
