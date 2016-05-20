Misk - базовый класс для базового класса виджетов
=================================================

.. py:class:: Misk()


    .. py:method:: bind(sequence=None, func=None, add=None)

        Привязывает событие к действию и возвращает идентификатор привязки

        * `sequence` - название события
        * `func` - обработчик, принимает ивент события, может возвращать строки "continue" и "break".

            Если функция возвращает "continue" то Tkinter продолжит обработку других привязок
            этого события,

            Если "break" - обработка этого события прекращается.

            Если функция ничего не возвращает (если возвращает None),
            то обработка событий продолжается (т.е. это эквивалентно возвращению "continue").

            * serial - серийный номер события (все события)
            * num - номер кнопки мыши (ButtonPress, ButtonRelease)
            * focus - имеет ли окно фокус (Enter, Leave)
            * height и width - ширина и высота окна (Configure, Expose)
            * keycode - код нажатой клавиши (KeyPress, KeyRelease)
            * state - состояние события (для ButtonPress, ButtonRelease, Enter, KeyPress, КeyRelease, Leave, Motion - в виде числа; для Visibility - в виде строки)
            * time - время наступления события (все события)
            * x и y - координаты мыши
            * x_root и y_root - координаты мыши на экране (ButtonPress, ButtonRelease, KeyPress, KeyRelease, Motion)
            * char - набранный на клавиатуре символ (KeyPress, KeyRelease)
            * send_event - см. документацию по X/Windows
            * keysym - набранный на клавиатуре символ (KeyPress, KeyRelease)
            * keysym_num - набранный на клавиатуре символ в виде числа (KeyPress, KeyRelease)
            * type - тип события в виде числа (все события)
            * widget - виджет, который получил событие (все события)
            * delta - изменение при вращении колеса мыши (MouseWheel)
        * `add` - добавить в цепочку обработчиков

        Список модификаторов

            * Control
            * Alt
            * Shift
            * Lock
            * Extended
            * Prior - PgUp
            * Next - PgDown
            * Button1, B1 - нажата первая (левая) кнопка мыши
            * Button2, B2 - вторая (средняя) кнопка мыши
            * Button3, B3 - третья (правая)
            * Button4, B4 - четвёртая
            * Button5, B5 - пятая
            * Mod1, M1, Command
            * Mod2, M2, Option
            * Mod3, M3
            * Mod4, M4
            * Mod5, M5
            * Meta, M
            * Double - двойной щелчок мыши (например, <Double-Button-1>)
            * Triple - тройной
            * Quadruple - четверной

        Типы событий

            * Activate, Deactivate
            * MouseWheel - прокрутка колесом мыши
            * KeyPress, KeyRelease - нажатие и отпускание клавиши на клавиатуре
            * ButtonPress, ButtonRelease, Motion - нажатие, отпускание клавиши мыши, движение мышью
            * Configure - изменение положения или размера окна
            * Map, Unmap - показывание или сокрытие окна (например, в случае сворачивания/разворачивания окна пользователем)
            * Visibility
            * Expose - событие генерируется, когда необходимо всё окно или его часть перерисовать
            * Destroy - закрытие окна
            * FocusIn, FocusOut - получение или лишение фокуса
            * Enter, Leave - Enter генерируется когда курсор мыши "входит" в окно, Leave - когда "уходит" из окна
            * Property
            * Colormap
            * MapRequest, CirculateRequest, ResizeRequest, ConfigureRequest, Create
            * Gravity, Reparent, Circulate

        .. code-block:: py

            widget.bind("<Control-Shift-KeyPress-q>", callback)

        .. code-block:: py

            """
            обработчик выбора элемента
            """
            def callback(val):
                listbox_widget = val.widget

            listbox.bind("<<ListboxSelect>>", callback)

        .. code-block:: py

            # обработчик клика для label
            label.bind('<Button-1>', lambda event: pass)


    .. py:method:: bind_all(sequence=None, func=None, add=None)

        Создаёт привязку для всех виджетов приложения.
        Отличие от привязки к окну верхнего уровня заключается в том,
        что в случае привязки к окну привязываются все виджеты этого окна,
        а этот метод привязывает все виджеты приложения (у приложения может быть несколько окон).


    .. py:method:: bind_class(className, sequence=None, func=None, add=None)

        Создаёт привязку для всех виджетов данного класса


    .. py:method:: bindtags(tagList)

        Позволяет изменить порядок обработки привязок.

        По умолчанию порядок следующий: виджет, класс, окно, all


    .. py:method:: clipboard_append(str)

        Добавляет в буфер текст


    .. py:method:: clipboard_clear()

        Очищает буфер обмена


    .. py:method:: config(**kwargs)
    .. py:method:: configure(**kwargs)

        Динамическая конфигурация виджета.

        Также можно использовать более краткую форму записи. используя квадратные скобки.

        Параметры аналогичны параметрам контсруктора

        .. code-block:: py

            button.config(text='new_text')
            button['command'] = new_command


    .. py:method:: grid_columnconfigure(index, cnf={}, **kw)
    .. py:method:: columnconfigure(index, cnf={}, **kw)

        Конфигурирование упаковщика

        * `minsize` - минимальная ширина/высота строки/столбца.

        * `weight` - "вес" строки/столбца при увеличении размера виджета. 0 означает, что строка/столбец не будет расширяться.
            
            Строка/столбец с "весом" равным 2 будет расширяться вдвое быстрее, чем с весом 1.
        
        * `uniform` - объединение строк/столбцов в группы. 

            Строки/столбцы имеющие одинаковый параметр uniform будут расширяться строго в соответствии со своим весом.

        * `pad` - размер бордюра. Указывает, сколько пространства будет добавлено к самому большому виджету в строке/столбце.


    .. py:method:: grid_location(x, y)

        Возвращает номер строки и столбца в которые попадают указанные координаты,
        либо -1 если координаты попали вне виджета.


    .. py:method:: grid_propagate()
    .. py:method:: grid_rowconfigure()
    .. py:method:: grid_size()

        Возвращает размер таблицы в строках и столбцах


    .. py:method:: grid_slaves()

        Возвращает список всех дочерних упакованных виджетов


    .. py:method:: pack_slaves()

        Возвращает список всех дочерних упакованных виджетов


    .. py:method:: pack_propagate(flag=['_noarg_'])

        Включает/отключает распространении информации о геометрии дочерних виджетов.

        По умолчанию виджет изменяет свой размер в соответствии с размером своих потомков.
        Этот метод может отключить такое поведение (pack_propagate(False)).

        Это может быть полезно, если необходимо,
        чтобы виджет имел фиксированный размер и не изменял его по прихоти потомков.


    .. py:method:: place_slaves()

        Возвращает список всех дочерних упакованных виджетов


    .. py:method:: unbind(sequence, funcid=None)

        Отвязать виджет от события. В качестве аргумента принимает идентификатор, полученный от метода bind.


    .. py:method:: unbind_all(sequence)

        Отвязать все виджеты от события


    .. py:method:: unbind_class(className, sequence)

        Отвязать все классы от события


    .. py:method:: winfo_height()

        Возвращает высоту элемента

        .. code-block:: py

            canvas.winfo_height()
            # 500


    .. py:method:: winfo_screenheight()

        Возвращает высоту рабочего области экарана в пикселях

        .. code-block:: py

            root.winfo_screenheight()
            # 1920


    .. py:method:: winfo_screenwidth()

        Возвращает ширину рабочего области экарана в пикселях

        .. code-block:: py

            root.winfo_screenwidth()
            # 3840


    .. py:method:: winfo_width()

        Возвращает ширину элемента

        .. code-block:: py

            canvas.winfo_width()
            # 500