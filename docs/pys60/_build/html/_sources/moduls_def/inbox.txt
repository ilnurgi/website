.. py:module:: inbox

inbox
=====

Модуль, позволяющий работать с сообщениями. Имеет доступ к папкам входящие, исходящие, отправленные и черновики.

.. py:class:: Inbox([folder_type]) 
    
    :param folder_type: тип папки с которой работать, по умолчанию inbox.EInbox
        
        * inbox.EInbox - работа с папкой Входящие;
        * inbox.EOutbox - работа с папкой Исходящие;
        * inbox.ESent - работа с папкой Переданные;
        * inbox.EDraft - работа с папкой Черновики.

    >>> box = inbox.Inbox()

.. py:method:: Inbox.address(sms_id) 

    :param sms_id: уникальный номер сообщения
    :type sms_id: int
    
    Возвращает адресата SMS сообщения
    
    >>> box.address(1048589)
    'ilnurgii'

.. py:method:: Inbox.bind(callback) 

    :param callback: обработчик
    :type sms_id: function
    
    Привязывает обработчик, при поступлении сообщения, передает в функцию 1 параметр, ID нового сообщения.

    >>> def print_id_sms(id):
            print id
    >>> box.bind(print_id_sms)

.. py:method:: Inbox.content(sms_id) 

    :param sms_id: уникальный номер сообщения
    :type sms_id: int
    
    Возвращает содержимое сообщения

    >>> box.content(1048589)
    'hello world'

.. py:method:: Inbox.delete(sms_id) 

    :param sms_id: уникальный номер сообщения
    :type sms_id: int
    
    Удаляет SMS сообщение
    
    >>> box.delete(1048589)

.. py:method:: Inbox.sms_messages() 
    
    Возвращает список ID SMS сообщений, находящихся в папке.

    >>> box.sms_messages()
    [..., 1048589, 1048586, 1048584, ...]

.. py:method:: Inbox.set_unread(sms_id, status) 
    
    :param sms_id: уникальный номер сообщения
    :type sms_id: int
    :param status: 0|1 прочтено|не прочтено
    
    Устанавливает статус SMS сообщение
    
    >>> box.set_unread(1048589, 1)

.. py:method:: Inbox.time(sms_id) 
    
    :param sms_id: уникальный номер сообщения
    :type sms_id: int
    
    Возвращает время создания SMS сообщения
    
    >>> box.time(1048589)
    1348454678.02

.. py:method:: Inbox.unread(sms_id) 

    :param sms_id: уникальный номер сообщения
    :type sms_id: int

    Возвращает статус SMS сообщение, (0 - если сообщение прочтено, 1 - если не прочтено).
    
    >>> box.unread(1048589)
    0