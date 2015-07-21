.. py:module:: laa

laa
===

Модуль для запуска любых приложений включая java приложения 
авторы: Maxim6630, kolayuk, watt 

.. py:method:: execute(uid)
    
    :param uid: uid приложения
    :type uid: int

    Запускает приложение

    >>> laa.execute(0xa0000bcd)
    # запускает x-plore

.. py:method:: execute_param(uid, param)

    :param uid: uid приложения
    :type uid: int    
    :param param: параметры запуска
    :type param: str

    Запускает приложение c параметром

    >>> laa.execute_param(0x10008d39, u'http://www.ilnurgi.ru/')
    # запускает стандартный браузер и переходит по ссылке

.. py:method:: about()
    
    Возвращает информацию о модуле
    
    >>> laa.about()
    # 'LAA - launch any app by Maxim6630 , v1.02'