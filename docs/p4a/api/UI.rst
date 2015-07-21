UI - работа с пользовательским интерфейсом
==========================================


.. py:method:: addContextMenuItem(str label, str event[ , Object eventData])

    добавляет новый элемент в контекстное меню, используется только при построении интерфейса через :py:meth:`webViewShow`


.. py:method:: addOptionsMenuItem(str label, str event[ , Object eventData, str iconName])

    добавляет новый элемент в меню

    >>> droid.addOptionsMenuItem(u'label', u'label_event')


.. py:method:: clearContextMenu()

    очищает контекстное меню


.. py:method:: clearOptionsMenu()

    очищает меню

    >>> droid.clearOptionsMenu()


.. py:method:: dialogCreateAlert([str title, str message])

    создает информационное окно, пустое, резельтат возвращается в виде события

    >>> droid.dialogCreateAlert()
    >>> droid.dialogShow()
    {
        u'data': {
            u'canceled': True
        }, 
        u'name': u'dialog', 
        u'time': 1407402590865000L
    }


.. py:method:: dialogCreateDatePicker([int year=1970, int month=1, int day=1])

    создает информационное окно выбора даты, ответ возваращается в виде события

    >>> droid.dialogCreateDatePicker()
    >>> droid.dialogShow()
    {
        u'data': {
            u'year': 1971, 
            u'day': 2, 
            u'which': u'positive', 
            u'month': 1
        }, 
        u'name': u'dialog', 
        u'time': 1407401126070000L
    }


.. py:method:: dialogCreateHorizontalProgress([str title, str message, int maximumProgress=100])

    создает информационное окно с горизонтальным прогрессбаром

    >>> droid.dialogCreateHorizontalProgress()
    >>> droid.dialogShow()


.. py:method:: dialogCreateInput([str title, str message, str defaultText, str inputType])

    создает информационное окно с текстовым полем, без кнопок, результат возвращается в виде события

    >>> droid.dialogCreateInput()
    >>> droid.dialogShow()
    {
        u'data': {
            u'canceled': True, 
            u'value': u'123'
        },
        u'name': u'dialog', 
        u'time': 1407401504232000L
    }


.. py:method:: dialogCreatePassword([str title, str message])

    создает информационное окно с текстовым полем для ввода пароля, без кнопок, резултат возвращается в виде события

    >>> droid.dialogCreatePassword()
    >>> droid.dialogShow()
    {
        u'data': {
            u'canceled': True, 
            u'value': u'123'
        },
        u'name': u'dialog', 
        u'time': 1407401504232000L
    }


.. py:method:: dialogCreateSeekBar(int startingValue, int maximumValue, str title, str message)

    создает информационное окно c полосой для выбора значения из промежутка, выбор а также перемещение возбуждают событие

    >>> droid.dialogCreateSeekBar()
    >>> droid.dialogShow()
    {
        u'data': {
            u'progress': 51, 
            u'which': u'seekbar', 
            u'fromuser': True
        }, 
        u'name': u'dialog', 
        u'time': 1407401975886000L
    }

.. py:method:: dialogCreateSpinnerProgress([str title, str message, int maximum_progress=100])

    создает информационное окно для ожидания

    >>> droid.dialogCreateSpinnerProgress()
    >>> droid.dialogShow()


.. py:method:: dialogCreateTimePicker([int hour=0, int minute=0, bool is24hour=false])

    создает информационное окно выбора времени, ответ возваращается в виде события

    >>> droid.dialogCreateSpinnerProgress()
    >>> droid.dialogShow()    
    {
        u'data': {
            u'hour': 12, 
            u'minute': 2, 
            u'which': u'positive'
        }, 
        u'name': u'dialog', 
        u'time': 1407402256633000L
    }


.. py:method:: dialogDismiss()

    закрывает информационное окно

    >>> droid.dialogDismiss()    


.. py:method:: dialogGetInput([str title='Value', str message='Please enter value:', str defaultText])

    создает информационное окно с текстовым полем, кнопками "ОК" и "Отмена", ответ возваращается в виде события

    >>> droid.dialogGetInput()
    {
        u'data': {
            u'which': u'positive', 
            u'value': u'123'
        }, 
        u'name': u'dialog', 
        u'time': 1407402335330000L
    }


.. py:method:: dialogGetPassword([str title='Password', str message])

    создает информационное окно с полем для ввода пароля, с кнопками "ОК" и "Отмена", ответ возваращается в виде события

    >>> droid.dialogGetPassword()
    {
        u'data': {
            u'which': u'positive', 
            u'value': u'123'
        }, 
        u'name': u'dialog', 
        u'time': 1407402335330000L
    }


.. py:method:: dialogGetResponse()

    возвращает :py:class:`Result` работы диалога, также возбуждает событие

    >>> droid.dialogGetResponse().result
    {
        u'data': {
            u'which': u'positive', 
            u'value': u'123'
        }, 
        u'name': u'dialog', 
        u'time': 1407402335330000L
    }

.. py:method:: dialogGetSelectedItems()

    возвращает результат выбора элементов из списка :py:meth:`dialogSetMultiChoiceItems`

    >>> droid.dialogGetSelectedItems().result
    [0, 1]


.. py:method:: dialogSetCurrentProgress(int current)

    устанавливает теукщее значение для диалога прогрессбара, созданного через :py:meth:`dialogCreateHorizontalProgress`

    >>> droid.dialogCreateHorizontalProgress()
    >>> droid.dialogShow()
    >>> for i in range(11):
            droid.dialogSetCurrentProgress(i*10)
            time.sleep(1)
    >>> droid.dialogDismiss()


.. py:method:: dialogSetItems(list items)

    устанавливает новый список элементов для окна запроса, результат выбора элемента возваращается в виде события

    >>> droid.dialogCreateAlert()
    >>> droid.dialogSetItems([u'1', u'2'])
    >>> droid.dialogShow()
    {
        u'data': {
            u'item': 0
        }, 
        u'name': u'dialog', 
        u'time': 1407405362417000L
    }


.. py:method:: dialogSetMaxProgress(int max)

    устанавливает новое максимальное значение для прогресбара, созданного через :py:meth:`dialogCreateHorizontalProgress`

    >>> droid.dialogCreateHorizontalProgress()
    >>> droid.dialogShow()
    >>> time.sleep(3)
    >>> droid.dialogSetMaxProgress(200)


.. py:method:: dialogSetMultiChoiceItems([list items, list selected])

    устанавливает новый список в информационное окно для множественного выбора

    >>> droid.dialogCreateAlert()
    >>> droid.dialogSetMultiChoiceItems([u'1', u'2'])
    >>> droid.dialogShow()


.. py:method:: dialogSetNegativeButtonText(str text)

    устанавливает новый текст для кнопки отрицания

    >>> droid.dialogCreateAlert()
    >>> droid.dialogSetMultiChoiceItems([u'1', u'2'])
    >>> droid.dialogSetNegativeButtonText(u'Отмена')
    >>> droid.dialogShow()


.. py:method:: dialogSetNeutralButtonText(str text)

    устанавливает текст для обычной кнопки

    >>> droid.dialogCreateAlert()
    >>> droid.dialogSetMultiChoiceItems([u'1', u'2'])
    >>> droid.dialogSetNeutralButtonText(u'Хорошо')
    >>> droid.dialogShow()

.. py:method:: dialogSetPositiveButtonText(str text)

    устанавливает текст для кнопки положительной

    >>> droid.dialogCreateAlert()
    >>> droid.dialogSetMultiChoiceItems([u'1', u'2'])
    >>> droid.dialogSetPositiveButtonText(u'ОК')
    >>> droid.dialogShow()

.. py:method:: dialogSetSingleChoiceItems(list items[ , int selected=0])

    устанавливает новый список для информационного окна с одиночным выбором

    >>> droid.dialogCreateAlert()
    >>> droid.dialogSetSingleChoiceItems([u'1', u'2'])
    >>> droid.dialogShow()


.. py:method:: dialogShow()

    отображает информационное окно

    >>> droid.dialogShow()

.. py:method:: fullDismiss()

    разрушает окно с активити

    >>> droid.fullDismiss()


.. py:method:: fullKeyOverride(list keycodes[, bool enable=True])

    перекрывает действия кнопок


.. py:method:: fullQuery()

    возваращает элементы текущего активити

    >>> droid.fullQuery()
    {
        u'button': {
            u'text': u'New Button', 
            u'type': u'Button', 
            u'id': u'button', 
            u'visibility': u'0'
        }, 
        u'text_view': {
            u'text': u'HelloWorld', 
            u'type': u'TextView', 
            u'id': u'text_view', 
            u'visibility': u'0'
        }
    }

.. py:method:: fullQueryDetail(str id)

    возвращает атрибуты виджета

    >>> droid.fullQueryDetail('button').result
    {
        u'text': u'New Button', 
        u'type': u'Button', 
        u'id': u'button', 
        u'visibility': u'0'
    }


.. py:method:: fullSetList(str id, list list)

    задает список для списка окна

    >>> droid.fullSetList('listView', ['123', '234'])


.. py:method:: fullSetProperty(str id, str property, str value)

    устанавливает новое свойство для виджета

    >>> droid.fullSetProperty("up_bar", "background", "file://.../res/Drawable/title.jpg")


.. py:method:: fullSetTitle(str title)

    устанавливает новый заголовок для текущего окна

    >>> droid.fullSetTitle(u'Заголовок новый')


.. py:method:: fullShow(str layout[ , str title])

    отображает активити

    >>> droid.fullShow('...xml_text...')


.. py:method:: makeToast(str message)

    создает всплывающее сообщение

    >>> droid.makeToast(u'Привет МИР')


.. py:method:: notify(str title, str message)

    создает уведомление

    >>> droid.notify(u'уведомление', u'привет')


.. py:method:: webViewShow(str url[ , bool wait])

    рисует интерфейс из html странички

    >>> droid.webViewShow("index.html")