.. py:module:: sysinfo2

sysinfo2
========

Питоновский модуль с системными функциями

.. versionadded:: pys60 2.0

.. py:method:: bt_power()
    
    Возвращает статус БТ
    
    >>> sysinfo2.bt_power()
    0

.. py:method:: bt_switch()  
    
    Включает/выключает БТ

.. py:method:: charger_status()  
    
    Возвращает статус зарядки
    
    >>> sysinfo2.charger_status()
    1

.. py:method:: launch_missed_calls()  
    
    Открывает стандартное приложение пропущенные вызовы.
    
    >>> sysinfo2.launch_missed_calls()

.. py:method:: list_access_points(0|1)  
    
    Возвращает список точек доступа (0 - все точки, 1 - то активная точка)
    
    >>> sysinfo2.list_access_points(0)
    [{'iapid': 2, 'active': 0, 'type': 2, 'name': u'\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435'}, {'iapid': 4, 'active': 0, 'type': 2, 'name': u'MegaFon MMS'}, {'iapid': 3, 'active': 0, 'type': 2, 'name': u'MegaFonPRO'}]

.. py:method:: new_email_status()  
    
    Возвращает 0=если нет новых сообщений, 1=есть новые сообщения, -1=ошибка 

.. py:method:: new_emails()  

.. py:method:: new_missed_calls()  
    
    Возвращает 0=если нет новых звонков, 1=есть новые сообщения, -1=ошибка

    >>> sysinfo2.new_missed_calls()
    0

.. py:method:: total_drivespace()  
    
    Возвращает размер дисков смартфона
    
    >>> .total_drivespace()
    {u'C:': 138928128, u'Y:': 1281536, u'D:': 89829376, u'Z:': 0, u'E:': 125861888}