.. py:module:: sysinfo

sysinfo
=======

Модуль для работы с системной информацией. 

.. py:method:: active_profile() 
    
    Возвращает активный профиль:
        * general – Обычный
        * silent – Без звука
        * meeting – Встреча
        * outdoor – На улице
        * pager – Пейджер
        * offline – Автономный
        * drive – В машине
        * user<profile_value> – пользовательский профиль (режим).
        * profile_value – имя профиля, заданное пользователем.
    
    >>> sysinfo.active_profile()
    'meeting'

.. py:method:: battery() 
    
    Возвращает число, уровень заряда аккумулятора в процентах
    
    >>> sysinfo.battery()
    100

.. py:method:: display_pixels() 
    
    Возвращает список, размеры экрана.
    
    >>> sysinfo.display_pixels()
    (360,640)

.. py:method:: display_twips() 
    
    Возвращает список, размеры экрана в твипсах (1/567 см).
    
    >>> sysinfo.display_twips()
    (2449,4354)

.. py:method:: free_drivespace() 
    
    Возвращает словарь, свободное пространство на дисках.
 
    >>> sysinfo.free_drivespace()
    {u'C:': 86908928, u'F:': 1373974528, u'D:': 115130368, u'Z:': 0, u'E:': 780959744}

.. py:method:: free_ram() 
    
    Возвращает число, свободное озу в байтах.
    
    >>> sysinfo.free_ram()
    115109888

.. py:method:: imei() 
    
    Возвращает строку, имей смартфона.
    
    >>> sysinfo.imei()
    u'1234567890123123'
    
.. py:method:: max_ramdrive_size() 
    
    По идее показывает максимальный размер диска D. но не работает у многих
    
    >>> sysinfo.max_ramdrive_size()

.. py:method:: os_version() 
    
    Возвращает список, версия операционной системы
    
    >>> sysinfo.os_version()
    (2,0,4067)

.. py:method:: ring_type() 
    
    Возвращает строку, тип сигнала.
        
        * normal – обычный
        * scending – нарастающий
        * ring once – одинарный
        * beep – короткий сигнал
        * silent – без звука
    
    >>> sysinfo.ring_type()
    'normal'

.. py:method:: signal_bars() 
    
    Возвращает число, уровень сигнала сети в уровнях от 0 до 7.
    
    >>> sysinfo.signal_bars()
    7

.. py:method:: signal_dbm() 
    
    Возвращает число, уровень сигнала сети в dBm
    
    >>> sysinfo.signal_dbm()
    74

.. py:method:: signal() 
    
    Возвращает число, неизвестно, похоже на signal_bars()
    
    >>> sysinfo.signal()
    7

.. py:method:: sw_version() 
    
    Возвращает строку, версию прошивки смарта.
    
    >>> sysinfo.sw_version()
    u'111.030.0607 2011-11-10 RM-596 (c) Nokia'

.. py:method:: total_ram() 
    
    Возвращает число, размер озу в байтах.
    
    >>> sysinfo.total_ram()
    20971502

.. py:method:: total_rom() 
    
    Возвращает число, размер диска Z (прошивка смарта) в байтах.
    
    >>> sysinfo.total_rom()
    20971502