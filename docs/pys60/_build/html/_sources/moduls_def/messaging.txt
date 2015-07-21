.. py:module:: messaging

messaging
=========

Модуль для работы с сообщениями 

.. py:method:: mms_send(number, text, attachment) 
    
    :param number: номер отправителя
    :param text: текст сообщения
    :param attachment: мультимедиа содержание

    Отправляет ммс сообщение
    
    >>> messaging.mms_send('1234567890', 'Hi', attachment='c:\\1.jpg')

.. py:method:: sms_send(number, text, [encoding='7bit', callback=None ]) 
    
    :param number: номер отправителя
    :param text: текст сообщения
    :param encoding: кодировка текста ('7bit', '8bit', 'UCS2')
    :param callback: обработчик отправки. Которому передается статус отправки: 

        * messaging.ECreated - создано;
        * messaging.EMovedToOutBox - перемещено в исходящие;
        * messaging.EScheduledForSend - ожидает отправки;
        * messaging.ESent - отправлено;
        * messaging.EDeleted - удалено из списка исходящих;
        * messaging.EScheduleFailed - ошибка с отправкой ждущего SMS;
        * messaging.ESendFailed - ошибка отправки (после нескольких неудачных попыток);
        * messaging.ENoServiceCentre - не задан SMS-центр;
        * messaging.EFatalServerError - фатальная ошибка.

    Отправляет сообщение

    .. note:: если callback не задан, то функция заблокирует выполнение потока до тех пор, пока сообщение не будет отправлено, либо отложено;
    
    .. note:: если будет совершена попытка отправить новое сообщение до того, как уйдет старое, произойдет ошибка RuntimeError.

    .. note:: если функция будет вызвана в автономном режиме, то сообщение станет в очередь и после подключения к сети оно будут отправлено (но, возможно, выйдет сообщение об ошибке).

    .. code-block:: python
        
        import messaging

        def cb(state):
            if state == messaging.ESent:
                print "**Message was sent**"
            if state == messaging.ESendFailed:
                print "**Something went wrong - Truly sorry for this**"
        messaging.sms_send("1234567", "Hello from PyS60!", '7bit', cb, "Mary")
        **Message was sent**
