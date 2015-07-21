.. py:module:: telephone

telephone
=========

Модуль позволяет осуществлять вызовы. 

.. py:method:: dial(number) 

    :param number: номер абонента
    :type number: unicode
    
    Осуществляет вызов. Если уже есть активный вызов, то он переводится в удержание. 

    .. warning:: перед вызовом желательно вызвать :py:meth: hang_up()

    .. code-block:: python

        try:
            telephone.hang_up()
        except:
            pass
        telephone.dial('1')

.. py:method:: hang_up() 
    
    Отбивает вызов (если вызов уже отбит, то произойдет ошибка SymbianError: KErrNotReady). 

.. py:method:: incoming_call() 
    
    Останавливает выполнение программы и ждет входящего вызова, после которого выполнение программы возобновляется (программа «засыпает» до первого звонка) 

.. py:method:: answer() 
    
    Отвечает на входящий вызов. После ответа и окончании разговора, желательно выполнить hung_up() 

.. py:method:: call_state(callable) 

    :param callable: обработчик

    Устанавливает обработчик состояния линии, в которую передается кортеж, абонент и статус линии.
        
        * telephone.EStatusUnknown - статус неизвестен;
        * telephone.EStatusIdle - нет активных вызовов;
        * telephone.EStatusDialling - осуществление вызова;
        * telephone.EStatusRinging - идут «гудки»
        * telephone.EStatusAnswering - ответ на вызов;
        * telephone.EStatusConnecting - подключение;
        * telephone.EStatusConnected - подключено;
        * telephone.EStatusReconnectPending - переподключение;
        * telephone.EStatusDisconnecting - отключение;
        * telephone.EStatusHold - отложено;
        * telephone.EStatusTransferring - перенаправление;
        * telephone.EStatusTransferAlerting - подключение к перенаправленному вызову.