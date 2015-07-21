.. py:module:: flashy

flashy
======

Модуль для отправки флеш сообщений. 
Что такое флэш сообщения? Получатель флэш SMS видит ваше сообщение сразу на экране после его прихода.

.. py:method:: version 
    
    Возвращает версию моуля
    
    >>> flashy.version
    (1,1,0)

.. py:method:: flashsms_send(number, message) 
    
    :param number: номер абонента
    :param message: текст сообщения

    Отправляет сообщение 

    >>> flashy.flashsms_send(u'1234567890', u'hello world')