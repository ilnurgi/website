.. py:module:: apptools

apptools
========

.. versionadded:: pys60 2.0

Модуль для работы с приложениями

.. py:method:: applaunch(app) 

    :param app: приложение
    :type app: unicode

    Запускает приложение
    
    >>> apptools.applaunch(0x10008d39)

.. py:method:: application_list(hidden, system) 

    :param hidden: 0|1 отображать скрытые
    :param system: 0|1 отображать системные    
    
    Возвращает кортеж запущенных приложений
    
    >>> apptools.application_list(0, 0)
    (u'PythonScriptShell', u'X-plore', u'\u0416\u0443\u0440\u043d\u0430\u043b', u'akncapserver', u'aknnfysrv', u'UpnpNotifAppServer')

.. py:method:: applist() 
    
    Возвращает список кортежей установленных приложений.
    
    >>> apptools.applist()
    [..., (536871485, u'Zip manager', u'Z:\\sys\\bin\\ZipManager.exe'), ...]

.. py:method:: end_app(app) 
    
    :param app: приложение
    :type app: unicode

    Закрывает приложение
    
    >>> apptools.end_app(u'Python')
    True

.. py:method:: fetchicon(uid, size, 1|2) 

    :param uid: uid запускаемого приложения
    :type uid: int
    :param size: размер
    :type size: tuple
    :param 1|2: иконка или маска

    Возвращает bitmap иконку приложения

    >>> bitmap_icon = apptools.fetchicon(0x10008d39, size, 1)
    >>> img = graphics.Image.from_cfbsbitmap(bitmap_icon)

.. py:method:: kill_app(app) 

    :param app: приложение
    :type app: unicode

    Убивает приложение
    
    >>> apptools.kill_app(u'Python')
    True

.. py:method::launchinbox([arg]) 

    :param args: 0x1002 - входящие, 0x1003 - исходящие, 0x1004 - черновики, 0x1005 - переданные
    :type args: int

    Открывает приложение "Сообщения"
    
    >>> apptools.launchinbox()
    True

.. py:method::launchsms(recipient, alias) 
    
    :param recipient: номер адрессата
    :type recipient: str
    :param alias: имя адрессата
    :type alias: unicode

    Запускает стандартное окно ввода сообщения
    
    >>> apptools.launchsms(u'89271234', u'Name')

.. py:method::missed_calls_log() 
    
    Запускает стандартное приложение пропущенных звонков.

.. py:method::switch_to_bg(app) 

    :param app: приложение
    :type app: unicode

    Сворачивает в фон приложение
    
    >>> apptools.switch_to_bg(u'Python')

.. py:method::switch_to_fg(app)     

    :param app: приложение
    :type app: unicode

    Делает активным приложение
    
    >>> apptools.switch_to_fg(u'Python')