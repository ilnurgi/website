BaseWidget - базовый виджет
===========================

.. py:class:: BaseWidget(**kwargs)

    Базовый виджет

    Наследник :py:class:`Misk`

    * `master` - :py:class:`Widget`, родительский виджет, если не задан используется окно приложения
    * `widgetName` - строка, название виджета
    * `cnf` - словарь
    * `kw` - словарь
        * `activebackground` - строка, цвет фона, когда виджет находится под курсором
        * `activeforeground` - строка, цвет текста, когда виджет находится под курсором
        * `anchor`
        * `background` - строка, цвет фона
        * `bg` - строка, цвет фона
        * `bitmap` - монохромное изображение виджета
        * `borderwidth` - число, ширина границы
        * `bd` - число, ширина границы
        * `cursor` - строка, тип курсора при наведении

            * arrow
            * circle
            * clock
            * cross
            * dotbox
            * exchange
            * fleur
            * heart
            * heart
            * man
            * mouse
            * pirate
            * plus
            * shuttle
            * sizing
            * spider
            * spraycan
            * star
            * target
            * tcross
            * trek
            * watch

        * `disabledforeground` - строка, цвет виджета, когда он выключен
        * `fg` - строка, цвет текста
        * `font` - строка, шрифт, 'Helvetica 20 italic' (bold, italic, underline, overstrike, roman, normal)
        * `foreground` - строка, цвет текста
        * `fg` - строка, цвет текста
        * `highlightbackground`
        * `highlightcolor` - цвет виджета, когда она в фокусе
        * `highlightthickness`
        * `image`
        * `justify` - константа :ref:`const_side`
        * `padx` - внутрений отступ по горизонтали
        * `pady` - внутрений отступ во вертикали
        * `relief` - константа :ref:`const_relief`
        * `repeatdelay`
        * `repeatinterval`
        * `takefocus`
        * `text`
        * `textvariable`
        * `underline` - подчеркивание, -1/1
        * `wraplength` - перенос длинного текста, -1/1
    * `extra` - словарь


    .. py:method:: after(time, callback)

        Таймер, выполняет функцию яерез определенное время.

        Возвращает идентификатор, который может быть использован в after_cancel.

        .. code-block:: py

            btn.after(200, tick)


    .. py:method:: after_idle(callback)

        Таймер, выполняет функцию после завершения всех отложенных операций
        (после того, как будут обработаны все события).

        Возвращает идентификатор, который может быть использован в after_cancel.

        .. code-block:: py

            btn.after_idle(tick)


    .. py:method:: after_cancel(timer_id)

        Отменяет указанное задание

        .. code-block:: py

            btn.after_cancel(1)


    .. py:method:: cget(key)

        Возвращает значение свойства объекта.

        Можно использовать и квадратные свойтсва.

        .. code-block:: py

            print btn.cget('text')
            # MyButton

        .. code-block:: py

            print btn['text']
            # MyButton


    .. py:method:: destroy()

        Уничтожает виджет и всех его потомков.

        .. code-block:: py

            btn.destroy()


    .. py:method:: focus()

        Передать фокус виджету.

        .. code-block:: py

            btn.focus()


    .. py:method:: focus_force()

        Передать фокус, даже если приложение не имеет фокуса.

        .. warning::

            Используйте осторожно, поскольку это может раздражать пользователей.

        .. code-block:: py

            btn.focus_force()


    .. py:method:: focus_get()

        Возвращает виджет, на который направлен фокус, либо None, если такой отсутствует.

        .. code-block:: py

            btn.focus_get()


    .. py:method:: focus_displayof()

        Возвращает виджет, на который направлен фокус на том дисплее,
        на котором размещён виджет, либо None, если такой отсутствует.

        .. code-block:: py

            btn.focus_displayof()


    .. py:method:: focus_lastfor()

        Возвращает виджет, на который будет направлен фокус, когда окно с этим виджетом получит фокус.

        .. code-block:: py

            btn.focus_lastfor()



    .. py:method:: grab_current()

        Получить виджет, который получает поток

        .. code-block:: py

            btn.grab_current()


    .. py:method:: grab_release()

        Освободить поток

        .. code-block:: py

            btn.grab_release()


    .. py:method:: grab_set()

        Передать поток данному виджету

        .. code-block:: py

            btn.grab_set()


    .. py:method:: grab_set_global()

        Передать глобальный поток данному виджету.

        В этом случае все события на дисплее будут передаваться этому виджету.

        .. warning::

            Следует пользоваться очень осторожно, т.к. остальные виджеты всех приложений не будут получать события.

        .. code-block:: py

            btn.grab_set_global()


    .. py:method:: grab_status()

        Узнать текущий статус потока событий для виджета.

        Возможные значения: None, "local" или "global".

        .. code-block:: py

            btn.grab_status()


    .. py:method:: tk_focusNext()

        Возвращает виджет, который получит фокус следующим (обычно смена фокуса происходит при нажатии клавиши Tab).
        Порядок следования определяется последовательностью упаковки виджетов.

        .. code-block:: py

            btn.tk_focusNext()


    .. py:method:: tk_focusPrev()

        То же, что и focusNext, но в обратном порядке.

        .. code-block:: py

            btn.tk_focusPrev()


    .. py:method:: tk_focusFollowsMouse()

        Устанавливает, что виджет будет получать фокус при наведении на него мышью.

        .. warning::

            Вернуть нормальное поведение достаточно сложно.

        .. code-block:: py

            btn.tk_focusFollowsMouse()


    .. py:method:: update()

        Обрабатывает все задачи, стоящие в очереди.

        Обычно эта функция используется во время "тяжёлых" расчётов,
        когда необходимо чтобы приложение оставалось отзывчивым на действия пользователя.

        .. code-block:: py

            btn.update()


    .. py:method:: update_idletasks()

        Выполняет задачи, обычно откладываемые "на потом", когда приложение будет простаивать.

        Это приводит к прорисовке всех виджетов, расчёту их расположения и т.д.

        Обычно эта функция используется если были внесены изменения в состояние приложения,
        и вы хотите, чтобы эти изменения были отображены на экране немедленно, не дожидаясь завершения сценария.

        .. code-block:: py

            btn.update_idletasks()