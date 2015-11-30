SMS - сообщение
===============

.. js:class:: SMS

    :js:func:`CreateSMS`


    .. js:function:: Send(number, msg)

        Отправляет сообщение на указанный номер

        
    .. js:function:: SetOnMessage(callback)

        Устанавливает обработчик входящих сообщений

        .. code-block:: js
            
            sms.SetOnMessage(function(number, msg){});


    .. js:function:: SetOnStatus(callback)

        Устанавливает обработчик изменения статуса сообщения

        .. code-block:: js
            
            sms.SetOnStatus(function(status){});