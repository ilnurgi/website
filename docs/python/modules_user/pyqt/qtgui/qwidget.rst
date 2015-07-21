.. py:module:: QtGui

QWidget - базовый виджет для всех интерфейсных объектов
=======================================================

.. py:class:: QWidget([parent=None][, flags=Qt.Widget])

    Виджет, пустая прямоуголная область. 

    Базовый объект для всех интерфесных объектов. 

    Наследник :py:class:`QtCore.QObject`, :py:class:`QtGui.QPaintDevice`.

    Если виджет не имеет родителя (parent), то виджет отображается как окно, иначе оно распологается на родительском виджете.

    Если в параметре `flags` указан тип окна, то компонент, имея родителя, будет обладать свои собственным окном, но привязан к родительскому окну. 

    Флаги виджета из класса :py:class:`QtCore.Qt`

        1. Widget - тип по умолчанию для класса QWidget;
        2. Window - указывает, что компонент является окном, независимо от того, имеет он родителя или нет. Окно выводится с рамкой и заголовком, в котором расположены кнопки Свернуть, Развернуть и Закрыть. По умолчанию размеры окна можно изменять с по­мощью мыши;
        3. Dialog - диалоговое окно. Окно выводится с рамкой и заголовком, в котором располо­жены кнопки Сnравка и Закрыть. Размеры окна можно изменять с помощью мыши.
        4. Sheet;
        5. Drawer;
        6. Popup - указывает, что окно является всплывающим меню. Окно выводится без рамки и заголовка. Кроме того, окно может отбрасывать тень. Изменить размеры окна с по­мощью мыши нельзя;
        7. Tооl- сообщает, что окно является панелью инструментов. Окно выводится с рамкой и заголовком (меньшем по высоте, чем обычное окно), в котором расположена кнопка Закрыть. Размеры окна можно изменять с помощью мыши;
        8. ToolTip - указывает, что окно является всплывающей подсказкой. Окно выводится без рамки и заголовка. Изменить размеры окна с помощью мыши нельзя;
        9. SplashScreen - сообщает, что окно является заставкой. Окно выводится без рамки и заголовка. Изменить размеры окна с помощью мыши нельзя. Значение по умолчанию для класса
        10. QSplashScreen;
        11. Desktop - указывает, что окно является рабочим столом. Окно вообще не отображается на экране;
        12. SubWindow - сообщает, что окно является дочерним компонентом, независимо от того, имеет он родителя или нет. Окно выводится с рамкой и заголовком (меньшем по высоте, чем обычное окно) без кнопок. Изменить размеры окна с помощью мыши нельзя.

    Для окон верхнего уровня можно дополнительно указать следующие атрибуты из класса :py:class:`QtCore.Qt` через оператор |:

        1. MSWindowsFixedSizeDialogHint - запрещает изменение размеров окна. Изменить раз­меры с помощью мыши нельзя. Кнопка Развернуть в заголовке окна становится неак­тивной;
        2. FramelessWindowHint - убирает рамку и заголовок окна. Изменять размеры окна и пе­ремещать его нельзя;
        3. CustomizeWindowHint - убирает рамку и заголовок окна, но добавляет эффект объем­ности. Размеры окна можно изменять с помощью мыши;
        4. WindowТitleНint - добавляет заголовок окна. 

            Например: выведем окно фиксированного размера с заголовком, в котором находится только текст:
    
                .. code-block:: py

                    window.setWindowFlags(
                        QtCore.Qt.Window |
                        QtCore.Qt.FramelessWindowHint |
                        9tCore.Qt.WindowТitleHint)

        5. WindowSystemМenuНint - добавляет оконное меню и кнопку Закрыть;
        6. WindowМinimizeButtonHint - кнопка Свернуть в заголовке окна делается активной, а кнопка Развернуть- неактивной;
        7. WindowМaximizeButtonHint - кнопка Развернуть в заголовке окна делается активной, а кнопка Свернуть неактивной;
        8. WinctowMinМaxButtonsHint - кноnки Свернуть и Развернуть в заголовке окна делаются активными;
        9. WindowCloseButtonHint - добавляет кноnку Закрыть;
        10. WindowContextHelpButtonHint - добавляет кноnку Справка. Кноnки Свернуть и Раз­вернуть в заголовке окна не отображаются;
        11. WindowStaysOnTopHint - сообщает системе, что окно всегда должно отображаться nо­верх всех других окон;
        12. WindowstaysonвottomНint - сообщает системе, что окно всегда должно расnоложено nозади всех других окон.


    .. py:method:: adjustSize()

        Подгоняет размеры компонента под содержимое. 

        При этом учитываются рекмендованные размеры, возвращаемые методом :py:meth:`sizeHint()`


    .. py:method:: baseSize()

        Возвращает :py:class:`QtCore.QSize`, базовые размеры компонента


    .. py:method:: close()

        Закрывает окно


    .. py:method:: frameGeometry()

        Возвращает :py:class:`QtCore.QRect`, содержащий координаты окна, включая высоту заголовка и ширину границ


    .. py:method:: frameSize()

        Возвращает :py:class:`QtCore.QSize`, размеры окна, включая высоту заголовка и ширину границ


    .. py:method:: geometry()

        Возвращает :py:class:`QtCore.QRect`, содержащий координаты относительно родительского объекта


    .. py:method:: height()

        Возвращает число, высоту компонента


    .. py:method:: hide()

        Скрывает окно


    .. py:method:: isEnabled()

        Возвращает истину/ложь, доступность объекта


    .. py:method:: isHidden()

        Возвращает истину/ложь, скрытость виджета


    .. py:method:: isVisible()

        Возвращает истину/ложь, видимость виджета


    .. py:method:: maximumHeight()

        Возвращает число, максимальную высоту компонента


    .. py:method:: maximumWidth()

        Возвращает число, максимальную ширину компонента


    .. py:method:: maximumSize()

        Возвращает :py:class:`QtCore.QSize`, максимальные размеры компонента


    .. py:method:: minimumHeight()

        Возвращает число, минимальную высоту компонента


    .. py:method:: minimumWidth()

        Возвращает число, минимальную ширину компонента


    .. py:method:: minimumSize()

        Возвращает :py:class:`QtCore.QSize`, минимальные размеры компонента


    .. py:method:: minimumSizeHint()

        Возвращает :py:class:`QtCore.QSize`, рекомендуемый минимальный размер компонента


    .. py:method:: move(x, y)
    .. py:method:: move(qpoint)

        :param int x: координата х
        :param int y: координата у
        :param QtCore.QPoint qpoint: объект, точка

        Изменяет положение компонента относительно родителя

    .. py:method:: palette()

        Возвращает :py:class:`QtGui.QPalette`, текущую палитру компонента. Для установки новой палитры компонента, необходимо воспользоваться методом :py:meth:`setPalette()`


    .. py:method:: parentWidget()

        возвращает родительский виджет


    .. py:method:: pos()

        Возвращает :py:class:`QtCore.QPoint`, содержащий координаты левого верхнего угла виджета, относительно родителя.


    .. py:method:: rect()

        Возвращает :py:class:`QtCore.QRect`, содержащий координаты и размеры прямоугольника, в который вписан компонент


    .. py:method:: repaint()
    .. py:method:: repaint(x, y, h, w)
    .. py:method:: repaint(qrect)
    .. py:method:: repaint(qregion)

        Незамедлительно вызывает метод :py:meth::`paintEvent()` для перерисовки компонента, при условии, что компонент не скрыт и обновление не запрещено с помощью метода :py:meth::`setUpdateEnabled()`


    .. py:method:: resize(h, w)
    .. py:method:: resize(qsize)

        :param int h: высота
        :param int w: ширина
        :param QtCore.QSize qsize: объект, размер
        
        Задает минимальные размеры виджета

    
    .. py:method:: setAutoFillBackgroud(bool)

        Включает автоматическию прорисовку фона. Компоненты-потомки имеют прозрачный фон и не перерисовываются автоматический


    .. py:method:: setAttribute(key, value)

        Изменяет атрибуты окна

        ::

            window.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)


    .. py:method:: setBaseSize(h, w)
    .. py:method:: setBaseSize(qsize)

        :param int h: высота
        :param int w: ширина
        :param QtCore.QSize qsize: объект, размер
        
        Задает базовый размер окна.
        

    .. py:method:: setDisabled(disabled)

        :param bool enabled: доступность объекта

        Управляет доступностью объекта, если объект не доступен, то генерация сигналов объекта выключена
        

    .. py:method:: setEnabled(enabled)

        :param bool enabled: доступность объекта

        Управляет доступностью объекта, если объект не доступен, то генерация сигналов объекта выключена


    .. py:method:: setGeometry(x, y, h, w)
    .. py:method:: setGeometry(qrect)

        :param int x: координата х
        :param int y: координата у
        :param int h: координата h
        :param int w: координата w
        :param QtCore.QRect qrect: объект, прямоуголная область

        Задает расположение окна и его размер. Метод не учитывает высоту заголовка и ширину границ.


    .. py:method:: setFixedHeight(h)

        :param int h: высота

        Задает фиксированную ширину окна. Изменить ширину окна мышкой нельзя.


    .. py:method:: setFixedWidth(w)

        :param int w: ширина

        Задает фиксированную высоту окна. Изменить высоту окна мышкой нельзя.


    .. py:method:: setFixedSize(h, w)
    .. py:method:: setFixedSize(qsize)

        :param int h: высота
        :param int w: ширина
        :param QtCore.QSize qsize: объект, размер

        Задает фиксированный размер окна. Изменить размеры окна мышкой нельзя, кнопка развернуть в заголовке становится не активной.


    .. py:method:: setLayout(layout)

        :param layout: лейаут (:py:class:`QtGui.QVBoxLayout`)

        Задает лейаут для виджета


    .. py:method:: setMaximumHeight(h)

        :param int h: высота

        Задает максимальную ширину окна.


    .. py:method:: setMaximumWidth(w)

        :param int w: ширина

        Задает максимальную высоту окна.


    .. py:method:: setMaximumSize(h, w)
    .. py:method:: setMaximumSize(qsize)

        :param int h: высота
        :param int w: ширина
        :param QtCore.QSize qsize: объект, размер

        Задает максимальный размер окна.


    .. py:method:: setMinimumHeight(h)

        :param int h: высота

        Задает минимальную ширину окна.


    .. py:method:: setMinimumWidth(w)

        :param int w: ширина

        Задает минимальную высоту окна.


    .. py:method:: setMinimumSize(h, w)
    .. py:method:: setMinimumSize(qsize)

        :param int h: высота
        :param int w: ширина
        :param QtCore.QSize qsize: объект, размер

        Задает минимальный размер окна.


    .. py:method:: setPalette(qpalette)

        :param qpalette: :py:class:`QtGui.QPalette`

        устанавливает палитру компонента


    .. py:method:: setParent(parent[, <ТипОкна>])

        Задает родителя для виджета


    .. py:method:: setStyleSheet()

        Изменяет стиль компонента

        ::

            label.setStyleSheet("background-color: #ffffff;")


    .. py:method:: setToolTip(text)

        Задает текст всплывающей подсказки


    .. py:method:: setVisible(bool)

        Отображает/скрывает виджет


    .. py:method:: setWhatsThis(текст)

        Задает текст справки компонента


    .. py:method:: setWindowFlags(flags)

        задает флаги виджета


    .. py:method:: setWindowIcon(qicon)

        отображает иконку в заголовке окна


    .. py:method:: setWindowTitle(text)

        Задает текст, который будет выводиться в заголовке окна


    .. py:method:: show()

        Отображает виджет


    .. py:method:: sizeHont()

        Возвращает :py:class:`QtCore.QSize`, рекомендуемые размеры компонента


    .. py:method:: tooltip()

        Возвращает текст всплывающей подсказки


    .. py:method:: update()
    .. py:method:: update(x, y, h, w)
    .. py:method:: update(qrect)
    .. py:method:: update(qregion)

        Посылает сообщение о необходимости перерисовки компонента.


    .. py:method:: whatsThis()

        Возвращает текст справки компонента


    .. py:method:: width()

        Возвращает число, ширину компонента


    .. py:method:: windowFlags()

        Возвращает все установленные флаги


    .. py:method:: windowType()

        Возвращает тип окна программы


    .. py:method:: x()

        Возвращает число, координату х верхнего левого угла виджета, относительно родителя


    .. py:method:: y()

        Возвращает число, координату у верхнего левого угла виджета, относительно родителя


    Фокус компонента
    ----------------


    .. py:staticmethod:: setTabOrder(qwidget1, qwidget2)

        Позволяет задать последовательность смены фокуса при нажатии <Tab>


    .. py:method:: clearFocus()

        Убирает фокус ввода с компонента


    .. py:method:: focusNextChild()

        Находит следующий компонент, которому можно передать фокус и передает фокус. Возвращает булево, комопонент найден или нет


    .. py:method:: focusNextChild(flag)

        Если flag=True, то метод анало­гичен методу :py:meth::`focusNextChild()`. Если flag=False, то метод анало­гичен :py:meth::`focusPreviousChild()`. Возвращает булево, комопонент найден или нет


    .. py:method:: focusPreviousChild()

        Находит предыдущий компонент, которому можно передать фокус и передает фокус. Возвращает булево, комопонент найден или нет


    .. py:method:: focusPolicy()

        Возвращает текущий способ получения фокуса


    .. py:method:: focusProxy()

        Возвращает ссылку на комонент, который обрабатывает фокус ввода вместто теущего компонента


    .. py:method:: focusWidget()

        Возвращает ссылку на последний компонент, для которого вызывался :py:meth::`setFocus()`


    .. py:method:: grapKeyboard()

        Захватывает ввод с клавиатуры. Другие компоненты не будут получать события клавиатуры, пока не будет вызван метод :py:meth::`releaseKeyboard()`


    .. py:method:: hasFocus()

        Возвращает булево, находится ли компонент в фокусе


    .. py:method:: setFocus([reason])

        Устанавливает фокус ввода

        * `reason` - причина изменения фокуса, атрибуты из класса :py:class::`QtCore.Qt`

            * `MouseFocusReason` - фокус изменен с помощью мыши
            * `TabFocusReason` - нажата клавиша <Таb>
            * `BacktabFocusReason` - нажата комбинация клавиш <Shift>+<Tab>
            * `ActiveWindowFocus` - окно стало активным или неактивным
            * `PopupFocusReason` - открыто или закрыто всплывающее окно
            * `ShortcutFocusReason` - нажата комбинация клавиш быстрого доступа
            * `MenuBarFocusReason` - фокус изменился из-за меню
            * `OtherFocusReason` - другая причина


    .. py:method:: releaseKeyboard()

        Освобождает захваченный ранее ввод с клавиатуры


    .. py:method:: setFocusPolicy(method)

        Задает способ получения фокуса компонентом.

        * `method` - атрибут из класса :py:class::`QtCore.Qt`

            * `NoFocus` - компонент не может получать фокус
            * `TabFocus` - с помощью клавиши <Tab>
            * `ClickFocus` - с помощью щелчка мыши
            * `StrongFocus` - <Tab> и щелчок мыши
            * `WheelFocus` - <Tab>, щелчок мыши и колесо мыши


    .. py:method:: setFocusProxy(qwidget)

        Позволяет указать ссылку на компонент, который будет получать фокус вода вместо текущего компонента


    Нажатие и отпускание клавиш на клавиатуре
    -----------------------------------------

    .. py:method:: keyPressEvent(event)

        :param event: .. py:class::`QKeyEvent`

        Вызывается при нажатии клавиш на клавиатуре


    .. py:method:: keyReleaseEvent(event)

        :param event: .. py:class::`QKeyEvent`

        Вызывается при отпускании ранее нажатой клавиши


    Клавиши быстрого доступа
    ------------------------

    Также можно назначить клавиши быстрого доступа с помощью классов :py:class::`QShortcut` или :py:class::`QAction`
    
    .. py:method:: grabShortcut(клавиши[, контекст])

        Регитсрирует клавиши быстрого доступа и возвращает идентификатор, с помощью которого можно управлять им в дальнейшем.

        * `клавиши` - :py:class::`QtGui.QKeySequence`

            .. code-block: py

                QtGui.QKeySequence.mnemonic("&e")
                QtGui.QKeySequence( "Alt+e")
                QtGui.QKeySequence(QtCore.Qt.ALT + QtCore.Qt.Key_E)

        * `контекст` - атрибут из :py:class::`QtCore.Qt`

            * `WidgetShortcut,` - 
            * `WidgetWithChildrenShortcut` - 
            * `WindowShortcut` - по умолчанию 
            * `ApplicationShortcut` - 


    .. py:method:: releaseShortcut(idi)

        Удаляет комбинацию с указанным идентификатором


    .. py:method:: setShortcutEnabled(idi[, flag])

        Включает/выключает клавиши быстрого доступа


    Ивенты компонентов
    ------------------


    .. py:method:: changeEvent(event)

        :param event: :py:class:`QWindowStateChangeEvent`, при обработке события `WindowStateChange`
        
        Обработчик изменения состояния окна, приложения или компонента.


    .. py:method:: closeEvent(event)

        :param event: :py:class:`QCloseEvent`
        
        Обработчик закрытия окна


    .. py:method:: event(event)

        :param event: :py:class:`QEvent`    

        Обработчик всех эвентов, возвращает `True` если событие принято, иначе `False`


    .. py:method:: focusInEvent(event)

        :param event: :py:class:`QFocusEvent`

        Эвент получнеия фокуса


    .. py:method:: focusOutIvent(event)

        :param event: :py:class:`QFocusEvent`   

        Эвент потери фокуса


    .. py:method:: hideEvent(event)

        :param event: :py:class:`QHideEvent`

        Обработчик скрытия компонента


    .. py:method:: moveEvent(event)

        :param event: :py:class:`QMoveEvent`

        Обработчик перемещения окна


    .. py:method:: paintEvent(event)

        :param event: :py:class:`QPaintEvent`

        Обработчик перерисовки компонента


    .. py:method:: resizeEvent(event)

        :param event: :py:class:`QResizeEvent`

        Обработчик изменения размера окна


    .. py:method:: showEvent(event)

        :param event: :py:class:`QShowEvent`

        Обработчик отображения компонента