Event - события
===============

Методы для работы с очередью событий. Очередь событий может содержать 1024 событий.

.. py:class:: Result()
    
    результат работы методов, событий

    
    .. py:attribute:: id

        идентификатор запроса


    .. py:attribute:: result

        ответ запроса


    .. py:attribute:: error

        ошибка запроса


.. py:method:: eventClearBuffer()

    очищает буфер событий


.. py:method:: eventGetBrodcastCategories()

    список всех событий


.. py:method:: eventPoll([int number_of_events=1])

    Возвращает и удаляет старые события


.. py:method:: eventPost(**kwargs)
 
    :param str name: название события
    :param str data: содержимое
    :param bool enqueue: не обязательный, по умолчанию null, если false, то событие не добавится в очередь а сразу выполнится

    отправляет событие в очередь


.. py:method:: eventRegisterForBroadcast(str category[ , bool enqueue])
 
    регистрирует слушателя для сигнала


.. py:method:: eventUnregisterForBroadcast(str category)

    удаляет слушателя для сигнала


.. py:method:: eventWait([int timeout])

    блокирует выполнение потока, до получения какого либо события: нажатие кнопок, вьюх и т.п. возвращает результат действия :py:class:`Result`, удаляя его из очереди событий

    >>> droid.eventWait().result
    # нажали кнопку смарта
    {
        u'data': {
            u'action': u'0', 
            u'key': u'4'
        }, 
        u'name': u'key', 
        u'time': 1407387781577000L
    }

    >>> droid.eventWait().result
    # кликнули по контролу
    {
        u'data': None, 
        u'name': u'label_event', 
        u'time': 1407400245808000L
    }

    * 4 - кнопка назад
    * 82 - кнопка меню


.. py:method:: eventWaitFor(str eventName[ , int timeout])

    блокирует выполнение потока, до получения указанного события: нажатие кнопок, вьюх и т.п. возвращает результат действия :py:class:`Result`, удаляя его из очереди событий


.. py:method:: startEventDispatcher([int port=0])

    Opens up a socket where you can read for events posted


.. py:method:: stopEventDispatcher()

    Stops the event server, you can't read in the port anymore