.. py:module:: positioning

positioning
===========

Модуль для работы с gps.

.. py:attribute:: POSITION_INTERVAL 
    
    Интервал в микросекундах (1000000=1 секунде), период обновления функции :py:meth:`position()`

.. py:method:: default_module() 
    
    Возвращает число, id установленного по умолчанию модуля гпс.

    >>> positioning.default_module()
    270526860

.. py:method:: last_position() 
    
    Возвращает последние данные о координатах. 

.. py:method:: modules() 
    
    Возвращает кортеж из словарей, доступных устройств на смартфоне.
    
    * 'available' - доступность устройства (0/1)
    * 'id' - номер устройства
        * 270526860 - AGPS
        * 270526858 - встроенный гпс
        * 270526873 - блютус гпс
        * 270559509 - данный на базе сети
        * 536979841 - wi-fi сеть
    * 'name' - имя устройства

    >>> positioning.modules()
    [{'available': 1, 'id': 270526860, 'name': u'A-GPS'},
     {'available': 1, 'id': 270526858, 'name': u'\u0412\u0441\u0442\u0440\u043e\u0435\u043d. \u043c\u043e\u0434\u0443\u043b\u044c GPS'},
     {'available': 0, 'id': 270526873, 'name': u'Bluetooth GPS'},
     {'available': 0, 'id': 536979841, 'name': u'Wi-Fi/\u0421\u0435\u0442\u044c'},
     {'available': 1, 'id': 270559509, 'name': u'\u041d\u0430 \u0431\u0430\u0437\u0435 \u0441\u0435\u0442\u0438'}]

.. py:method:: module_info(module_id) 
    
    Возвращает словарь, информацию, о модуле

    >>> positioning.module_info(270526860)
    {'available': 1, 'status': {'data_quality': 1, 'device_status': 3}, 'name': u'A-GPS', 'position_quality': {'time_to_first_fix': 1000000L, 'cost': 2, 'horizontal_accuracy': 10.0, 'vertical_accuracy': 10.0, 'time_to_next_fix': 1000000L, 'power_consumption': 3}, 'capabilities': 127, 'version': u'1.00(0)', 'location': 1, 'technology': 4, 'id': 270526860}

.. py:method:: select_module(module_id) 
    
    Устанавливает стандартным модуль
    
    >>> positioning.select_module(270526680)

.. py:method:: set_requestors() 
    
    хз, без этой функции не работает приемник и надо передать параметры из примера

    >>> positioning.set_requestors([{'type':'service', 'format':'application', 'data':'test_app'}])

.. py:method:: position(course=0,satellites=0,callback=None, interval=positioning.POSITION INTERVAL, partial=0) 

    :param course: 0|1 информация о курсе
    :param satellites: 0|1 информация о спутнике
    :param callback: обработчик координат
    :param interval: время в микросекундах, через которые будут передаваться координаты
    :param partial: 0|1 в обработчик придет информация о спутниках, перед расчетом местоположения

    Возвращает словарь, координаты позиции с gps

    >>> positioning.position()
    {'satellites': None, 'position': {'latitude': 65.815685987472534, 'altitude': 90.0, 'vertical_accuracy': 230.45707702636719, 'longitude': 47.181628227233887, 'horizontal_accuracy': 298.0}, 'course': None}
    
    >>> positioning.position(course=1, satellites=1, callback=positioncb, interval=1000000*10, partial=1) 
    
    {'satellites': {'horizontal_dop': 0.85, 'used_satellites': 4, 'vertical_dop': 0.8, 'time': 1376044235.0, 'satellites': 6, 'time_dop': 0.5199}, 'position': {'latitude': 65.815685987472534, 'altitude': 90.0, 'vertical_accuracy': 230.45707702636719, 'longitude': 47.181628227233887, 'horizontal_accuracy': 298.0}, 'course': {'speed': 0, 'heading': nan, 'heading_accuracy': nan, 'speed_accurace': 0}}

.. py:method:: stop_position() 

    Останаливает запущенную функцию :py:meth:`position()`
    Почему то у меня он не заработал, с ним вываливается весь скрипт, так что будьте аккуратней 

Пример
------

.. code-block:: python
 
    import positioning
    positioning.set_requestors([{"type":"service", "format":"application", "data":"test_app"}])
    print positioning.position()
    # {'satellites': None, 'position': {'latitude': 40.111924347701, 'altitude':147.5, 'vertical_accuracy': 120.0, 'longitude': -88.228399329257, 'horizontal_accuracy': 71.9983825683594}, 'course': None}