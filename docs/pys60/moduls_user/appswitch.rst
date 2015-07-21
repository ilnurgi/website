.. py:module:: appswitch

appswitch
=========

Модуль для работы с приложениями 

.. py:method:: application_list(hidden)

    :param hidden: 0|1 показ скрытых процессов

    Возвращает кортеж юникод строк запущенных прложений

    >>> appswitch.application_list(0)
    (u'PythonScriptShell', u'X-plore', u'Python', ... ) 
    >>> appswitch.application_list(1)
    (u'PythonScriptShell', u'EiksrvBackdrop', u' ' ... )

.. py:method:: end_app(app)

    :param app: приложение
    :type app: unicode
    
    Завершает работу приложения
    
    >>> appswitch.end_app(u'Python')
    True

.. py:method:: kill_app(app) 
    
    :param app: приложение
    :type app: unicode

    Убивает приложение
    
    >>> appswitch.kill_app(u'Python')
    True

.. py:method:: kill_process(app)
    
    .. versionadded:: pys60 1.4.5 
    
    :param app: приложение
    :type app: unicode

    Убивает процесс
    
    >>> appswitch.kill_process(u'Menu*')
    True
    >>> appswitch.kill_process(u"*101f4cd2*")

.. py:method:: process_list()

    .. versionadded:: pys60 1.4.5 

    Возвращает кортеж юникод строк запущенных процессов
    
    >>> appswitch.process_list()
    (u'ekern.exe[100041af]0001', u'efile.exe[100039e3]0001', u'domainSrv.exe[1020e406]0001', ... ) 

.. py:method:: switch_to_bg(app) 

    :param app: приложение
    :type app: unicode

    Сворачивает в фон приложение

    >>> appswitch.switch_to_bg(u'Python')
    True

.. py:method:: switch_to_fg(app) 

    :param app: приложение
    :type app: unicode    

    Разворачивает из фона приложение app, app в юникоде
    
    >>> appswitch.switch_to_fg(u'Python')
    True
