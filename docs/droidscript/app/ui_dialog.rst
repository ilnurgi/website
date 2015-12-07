Диалоговые, информационные окна
===============================

.. js:function:: app.Alert(text, title)

    Отображает информационное окно

    .. code-block:: js
        
        app.Alert('Hello World!', 'Message');


.. js:function:: app.CreateDialog(title, options)

    Возвращает :js:class:`Dialog`, компонент диалога.

    * `options`

        * `NoCancel` - диалоговое окно без кнопки Отмена, при клике вне области диалога, диалоговое окно закроется

        * `NoTitle` - диалоговоеокно без заголовка

    .. code-block:: js
        
        dlgL = app.CreateDialog('Chose item');
        dlgL = app.CreateDialog('Chose item', 'NoCancel');


.. js:function:: app.CreateListDialog(title, list, options)

    Возвращает :js:class:`ListDialog`

    .. code-block:: js
        
        dlg = app.CreateListDialog('Choises', 'Add,Remove')
        dlg = app.CreateListDialog('Choises', 'Add,Remove', 'Multi')


.. js:function:: app.CreateNotification(options)

    Возвращает :js:class:`Notification`

    * `options` 

        * `AutoCancel` - уведомление пропадет после прочтения

        * `FullScreen` - 

        * `Ongoing` - This option creats an ongoing notification in the status bar

    .. code-block:: js
        
        notify = app.CreateNotification();
        notify = app.CreateNotification('AutoCancel');
        notify = app.CreateNotification('AutoCancel,FullScreen');


.. js:function:: app.CreateShortcut(name, icon, script)

    Создает ярлык на рабочем экране устройства
    
    .. code-block:: js
        
        app.CreateShortcut("Hello World", "/mnt/sdcard/DroidScript/Hello World/Img/Hello World.png", "/mnt/sdcard/DroidScript/Hello World/Hello World.js");


.. js:function:: app.CreateYesNoDialog(msg)

    Возвращает :js:class:`YesNoDialog`, диалоговое окно с выбором Да/Нет

    .. code-block:: js
        
        yesNo = app.CreateYesNoDialog('Yes?')


.. js:function:: app.GetNotifyId()   

    Возвращает идентификатор уведомления


.. js:function:: app.HideProgress()

    Скрывает показанные прогресс, :js:func:`ShowProgress`

    .. code-block:: js
        
        app.HideProgress();


.. js:function:: app.HideProgressBar()

    Скрывает показанные прогрессбар, :js:func:`ShowProgressBar`, :js:func:`UpdateProgressBar`

    .. code-block:: js
        
        app.HideProgressBar();


.. js:function:: app.ShowPopup(text, options)

    Отображает всплывающее сообщение

    * `options`

        * `Short`
        * `Bottom`

    .. code-block:: js
        
        app.ShowPopup('Hello World', 'Bottom,Short');


.. js:function:: app.ShowProgress(text)

    Отображает прогресс с текстом, :js:func:`HideProgress`

    .. code-block:: js
        
        app.ShowProgress('Loading ...');
        setTimeout('app.HideProgress()', 3000);


.. js:function:: app.ShowProgressBar(text)

    Отображает прогрессбар с текстом, :js:func:`HideProgressBar`, :js:func:`UpdateProgressBar`

    .. code-block:: js
        
        app.ShowProgressBar('Loading ...');
        setTimeout('app.HideProgressBar()', 3000);


.. js:function:: app.UpdateProgressBar(progress)

    Включает вибрацию по указанному паттерну, :js:func:`ShowProgressBar`, :js:func:`HideProgressBar`

    .. code-block:: js
        
        app.UpdateProgressBar(60);