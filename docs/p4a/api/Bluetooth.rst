Bluetooth
=========

.. py:method:: bluetoothAccept(str uid, int timeout)

    :param str uuid: не обязательный, по дефолту 457807c0-4897-11df-9879-0800200c9a66, uuid устройства
    :param int timeout: не обязательный, по дефолту 0, время доступности

    включает блютус в режим доступности


.. py:method:: bluetoothActiveConnections()

    возвращает активные сенаснсы


.. py:method:: bluetoothConnect(str uuid, str address)

    :param str uuid: не обязательный, по дефолту 457807c0-4897-11df-9879-0800200c9a66, uuid устройства
    :param str address: не обязательный,  The user will be presented with a list of discovered devices to choose from if an address is not provided
    :return: True|False

    соединяется с устройством


.. py:method:: bluetoothDiscoveryCancel()
    
    :return: True|False

    выключает доступность БТ


.. py:method:: bluetoothDiscoveryStart()

    :return: True|False

    включает доступность БТ


.. py:method:: bluetoothGetConnectedDeviceName(str connID)

    :param str connID: не обязательный, по дефолту null, иди соединения

    возвращает имя соединенного устройства


.. py:method:: bluetoothGetLocalAddress()

    возвращает адрес локального БТ устройства


.. py:method:: bluetoothGetLocalName()

    возвращает имя доступного БТ устройства


.. py:method:: bluetoothGetRemoteDeviceName(str address)
    
    :param str address: адрес доступного БТ устройства

    возвращает имя удаленного устройства устройства или null


.. py:method:: bluetoothGetScanMode()

    возвращает статус текущего устройства

    -1 when Bluetooth is disabled.
    0 if non discoverable and non connectable.
    1 connectable non discoverable.
    3 connectable and discoverable.


.. py:method:: bluetoothIsDiscovering()

    возвращает True|False, БТ в режиме доступности


.. py:method:: bluetoothMakeDiscoverable([int duration])
 
    :param int duration: не обязательный, по дефолту 300, время доступности БТ

    опроверяет, имеется ли возможность сделать БТ доступ на указанное время


.. py:method:: bluetoothRead([int bufferSize, str connID])
    
    :param int bufferSize: не обязательный, по дефолту 4096, размер буфера для чтения
    :param str connID: не обязательный, по дефолту null, иди соединения

    читает данные из БТ


.. py:method:: bluetoothReadBinary([int bufferSize, str connID]
 
    :param int bufferSize: не обязательный, по дефолту 4096, размер буфера для чтения
    :param str connID: не обязательный, по дефолту null, иди соединения

    читает данные из БТ и djpdhfoftn chunked, base64 encoded String.


.. py:method:: bluetoothReadLine([str connID])

    :param str connID: не обязательный, по дефолту null, иди соединения

    читает следующую порцию


.. py:method:: bluetoothReadReady([str connID])

    :param str connID: не обязательный, по дефолту null, иди соединения

    возвращает True, если БТ доступен для чтения


.. py:method:: bluetoothSetLocalName([str name])

    задает новое имя для доступного БТ устройства


.. py:method:: bluetoothStop([str connID])
    
    :param str connID: не обязательный, по дефолту null, иди соединения

    закрывает БТ соедение


.. py:method:: bluetoothWrite(str ascii[ , str connID])

    :param str ascii: текст
    :param str connID: не обязательный, по дефолту null, иди соединения

    отправляет ascii данные через БТ


.. py:method:: bluetoothWriteBinary(str base64[ , str connID])

    :param str base64: base64 данные
    :param str connID: не обязательный, по дефолту null, иди соединения

    отправляет данные по БТ


.. py:method:: checkBluetoothState()

    True|False, БТ включен


.. py:method:: toggleBluetoothState([bool enabled, bool prompt])

    :param bool enabled: не обязательный, 
    :param bool prompt: не обязательный, по дефолту true, запрос у пользователя на изменение состояния БТ

    Вкл/выкл БТ