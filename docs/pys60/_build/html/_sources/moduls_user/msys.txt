.. py:module:: msys

msys
====

Модуль для работы с системными функциями

.. py:attribute:: KMaxVibration
    
    .. versionadded:: pys60 2.0
    
    Максимальное значение вибрации 

.. py:attribute:: KMinVibration 
    
    .. versionadded:: pys60 2.0

    Минимальное значение вибрации 

.. py:attribute:: language 
    
    .. versionadded:: pys60 2.0
    
    Возвращает номер языка активного на смарте
    
    >>> msys.language
    16

.. py:method:: active_connections()  

    .. versionadded:: pys60 2.0 
    
    Возвращает активное соединение
    
    >>> msys.active_connections()
    None

.. py:method:: closeapp(app) 

    :param app: название приложения
    :type app: unicode
    
    Закрывает приложение
    
    >>> msys.close_app(u'Python')
    True

.. py:method:: exit_text(text)             
    
    .. versionadded:: pys60 2.0 
    
    Текст на правой софт клавише
    
    >>> msys.exit_text(u'Выход')
    u'Exit'

.. py:method:: imsi()             
    
    .. versionadded:: pys60 2.0 
    
    Возвращает imsi смартфона
    
    >>> msys.imsi()
    u'250027413097373'

.. py:method:: infotask(uid)             
    
    .. versionadded:: pys60 2.0 
    
    Возвращает словарь-информацию о процессе, с ключами Path, UID, Name, Short Name
    
    >>> msys.infotask(u'0xa0000bcd')
    {'Path': u'C:\\sys\\bin\\X-plore.exe', 'UID': u'0xA0000BCD', 'Name': u'X-plore', 'Short Name': u'X-plore'}

.. py:method:: is_hidden() 

    Возвращает 1/0 если приложение скрыто/не скрыто из диспетчера
    
    >>> msys.is_hidden()
    0
    
.. py:method:: is_system() 
    
    Возвращает 1/0 если приложение системное/не системное
    
    >>> msys.is_system()
    0

.. py:method:: isrunning(app) 
    
    Проверяет, запущена ли программа
    
    >>> msys.isrunning(u'Python')
    1

.. py:method:: key_lock()             
    
    .. versionadded:: pys60 2.0 
    
    Блокирует смартфон без уведомления
    
    >>> msys.key_lock()
    True

.. py:method:: key_lock_silent()
    
    .. versionadded:: pys60 2.0 
    
    Блокирует смартфон с уведомлением

.. py:method:: key_status()             
        
    .. versionadded:: pys60 2.0 
    
    Возвращает статус блокировки клавиатуры
    
    >>> msys.key_status()
    0

.. py:method:: key_unlock()             
        
    .. versionadded:: pys60 2.0 
    
    Разблокирует смартфон без уведомления
    
    >>> msys.key_unlock()
    True

.. py:method:: key_unlock_silent()             
        
    .. versionadded:: pys60 2.0 
    
    Разблокирует смартфон с уведомлением

.. py:method:: kill_process(proc)             
    
    .. versionadded:: pys60 2.0 
    
    Убивает процесс

    >>> msys.kill_process(u'Phonebook.exe[101f4cce]0001')
    True

.. py:method:: killapp(app) 
    
    Убивает приложение
    
    >>> msys.killapp(u'Python')
    True

.. py:method:: listapp()             
    
    .. versionadded:: pys60 2.0 

    Возвращает список кортежей установленных приложений на смартфоне.
    
    >>> msys.listapp()
    [..., (u'Adobe Reader', u'0x20001BB9', u'Z:\\sys\\bin\\AdobeReader.exe'), ...]

.. py:method:: listtask(hidden=0|1)             
    
    .. versionadded:: pys60 2.0 
    
    Возвращает кортеж запущенных процессов
    
    >>> msys.listtask(0)
    ((u'PythonScriptShell', u'0xe7881dfa'), ...)

.. py:method:: navitext(text)             
    
    .. versionadded:: pys60 2.0 
    
    Текст в навигационной панели

    >>> msys.navitext(u'Навигация')

.. py:method:: option_text(text)             
    
    .. versionadded:: pys60 2.0 

    Текст на левой софт клавише меню, text юникод строка

    msys.option_text(u'Меню')

.. py:method:: process()             
    
    .. versionadded:: pys60 2.0 

    Возвращает кортеж запущенных процессов

    >>> msys.process()
    ( ... , (u'483', u'Phonebook.exe[101f4cce]0001', u'Z:\\sys\\bin\\Phonebook.exe'), ... )

.. py:method:: send_bg() 
    
    Скрывает/убирает в фон приложение
    
    >>> msys.send_bg()

.. py:method:: send_fg() 
    
    Показывает/выводит на экран приложение
    
    >>> msys.send_fg()

.. py:method:: set_hidden([1/0])             
        
    
    Скрывает/показывает приложение из диспетчера
    
    >>> msys.set_hidden(1)

.. py:method:: set_system([1|0])
    
    Делает приложение системным/не системным
    
    msys.set_system(1)

.. py:method:: switch_to_bg(app)             
    
    .. versionadded:: pys60 2.0 

    Скрывает/убирает в фон приложение
    
    >>> msys.switch_to_bg(u'Python')
    
.. py:method:: switch_to_fg(app)             
    
    .. versionadded:: pys60 2.0 
    
    Показывает/выводит на экран приложение
    
    >>> msys.switch_to_fg(u'Python')

.. py:method:: thread()             
    
    .. versionadded:: pys60 2.0 

.. py:method:: version()             
    
    .. versionadded:: pys60 2.0 

    Возвращает версию модуля

    >>> msys.version()
    u'0.9.5'

.. py:method:: vibra(vibration)             
    
    .. versionadded:: pys60 2.0 
    
    Вибрация смартфона, vibration - сила вибрации 

.. py:method:: unset_hidden()

    Показывает приложение в диспетчере
    
    >>> msys.unset_hidden()

.. py:method:: unset_system()
    
    Делает приложение не системным
    
    >>> msys.unset_system()