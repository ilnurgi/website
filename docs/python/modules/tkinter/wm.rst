VM - менеджер окон
==================

.. py:class:: WM()

    Менеджер окон


    .. py:method:: deiconify()
    .. py:method:: wm_deiconify()

        Разворачивает окно из панели задач

        .. code-block:: py

            root.iconify()


    .. py:method:: frame()
    .. py:method:: wm_frame()

        Возвращает идентификатор окна


    .. py:method:: geometry(newGeometry=None)
    .. py:method:: wm_geometry(newGeometry=None)

        Устанавливает геометрию окна в формате ШИРИНАxВЫСОТА+Х+У.

        Если не задаы параметры, то возвращает текущие размеры и координаты.

        .. code-block:: py

            # поместить окно в точку с координатам 40,80 и установить размер в 600x400
            top_level.geometry("600x400+40+80")

            # только изменить размер
            top_level.geometry("600x400")

            # только переместить окно
            top_level.geometry("+40+80")

        .. code-block:: py

            import re

            def parsegeometry(geometry):
                m = re.match("(\d+)x(\d+)([-+]\d+)([-+]\d+)", geometry)
                if not m:
                    raise ValueError("failed to parse geometry string")
                return map(int, m.groups())
            width, height, x, y = parsegeometry(root.geometry())


    .. py:method:: group(pathName=None)
    .. py:method:: wm_group(pathName=None)

        Возвращает группу окна или назначает группу


    .. py:method:: iconify()
    .. py:method:: wm_iconify()

        Сворачивает окно в панель задач

        .. code-block:: py

            top_level.iconify()


    .. py:method:: lift(aboveThis=None)
    .. py:method:: tkraise(aboveThis=None)

        Поднимает (размещает поверх всех других окон) окно, над каким-то окном.

        .. code-block:: py

            root.lift()


    .. py:method:: lower(aboveThis=None)

        Опускает окно, под каким-то окном.

        .. code-block:: py

            root.lower()


    .. py:method:: maxsize(width=None, height=None)
    .. py:method:: wm_maxsize(width=None, height=None)

        Устанавливает максимальные размеры окна, если они заданы, иначе возвращает текущие.

        .. code-block:: py

            root.minsize()


    .. py:method:: minsize(width=None, height=None)
    .. py:method:: wm_minsize(width=None, height=None)

        Устанавливает минимальные размеры окна, если они заданы, иначе возвращает текущие.

        .. code-block:: py

            root.minsize()


    .. py:method:: overrideredirect(boolean=None)
    .. py:method:: wm_overrideredirect(boolean=None)

        Указание оконному менеджеру игнорировать это окно.

        В случае, если аргумент не указан - получаем текущее значение.

        Если аргумент равен True, то такое окно будет показано оконным менеджером без обрамления (без заголовка и бордюра).

        .. note::

            Может быть использовано, например, для создания splashscreen при старте программы.

        .. code-block:: py

            root.overrideredirect()


    .. py:method:: positionfrom(who=None)
    .. py:method:: wm_positionfrom(who=None)



    .. py:method:: protocol(name=None, func=None)
    .. py:method:: wm_protocol(name=None, func=None)

        Устанавливает обработчик указанного события.

        События могут быть:

            * `WM_TAKE_FOCUS` - получение фокуса
            * `WM_SAVE_YOURSELF` - необходимо сохраниться, в настоящий момент является устаревшим
            * `WM_DELETE_WINDOW` - удаление окна

        .. code-block:: py

            def window_deleted():
                # do some
                root.destroy()

            root.protocol('WM_DELETE_WINDOW', window_deleted)


    .. py:method:: resizable(width=None, height=None)
    .. py:method:: wm_resizable(width=None, height=None)

        Задает возможность изменения размера окна, или возвращает текушее.

        .. code-block:: py

            root.resizable(True, False)


    .. py:method:: sizefrom(who=None)
    .. py:method:: wm_sizefrom(who=None)


    .. py:method:: state(newstate=None)
    .. py:method:: wm_state(newstate=None)

        Устанавливает новое состояние окна, если не задано, возвращает текущее:

            * `normal` - нормальное состояние
            * `iconic` - свёрнуто
            * `withdrawn` - не показано

        .. code-block:: py

            root.state()


    .. py:method:: title(string=None)
    .. py:method:: wm_title(string=None)

        Устанавливает заголовок окна

        .. code-block:: py

            root.title('My window')


    .. py:method:: transient(master=None)
    .. py:method:: wm_transient(master=None)

        Сделать окно зависимым от другого окна, указанного в аргументе.
        Будет сворачиваться вместе с указанным окном.

        Без аргументов возвращает текущее значение.

        .. code-block:: py

            root.transient()


    .. py:method:: withdraw()
    .. py:method:: wm_withdraw()

        Cпрятать (сделать невидимым) окно. Для того, чтобы снова показать его, надо использовать метод deiconify.

        .. code-block:: py

            root.withdraw()