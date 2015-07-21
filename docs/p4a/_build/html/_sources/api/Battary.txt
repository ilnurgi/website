Battery
=======

Перед вызовом методов batteryGet*, необходимо выполнить метод :py:meth:`batteryStartMonitoring` и дождаться ответа.

Результат работы всех методов :py:class:`Result`

>>> droid.batteryStartMonitoring()


.. py:method:: batteryCheckPresent()

    возвращает статус мониторинга батареи

    >>> droid.batteryCheckPresent().result
    None
    >>> droid.batteryStartMonitoring().result
    None
    >>> droid.batteryCheckPresent().result
    True


.. py:method:: batteryGetHealth()

    возвращает уровень заряда батареи

        * 1 - unknown
        * 2 - good
        * 3 - overheat
        * 4 - dead
        * 5 - over voltage
        * 6 - unspecified failure

    >>> droid.batteryGetHealth().result
    2


.. py:method:: batteryGetLevel()

    возвращает уровень зарядя батареи в процентах

    >>> droid.batteryGetLevel().result
    50


.. py:method:: batteryGetPlugType()

    возвращает тип устройства, откуда идет зарядка

        * -1 - unknown
        * 0 - unplugged
        * 1 - power source is an AC charger
        * 2 - power source is a USB port

    >>> droid.batteryGetPlugType().result
    1


.. py:method:: batteryGetStatus()

    возвращает статус зарядки

        * 1 - unknown
        * 2 - charging
        * 3 - discharging
        * 4 - not charging
        * 5 - full

    >>> droid.batteryGetStatus().result
    2


.. py:method:: batteryGetTechnology()

    возвращает тип аккумулятора

    >>> droid.batteryGetTechnology().result
    Li-ion


.. py:method:: batteryGetTemperature()

    возвращает температуру батареи

    >>> droid.batteryGetTemperature().result
    0


.. py:method:: batteryGetVoltage()

    возвращает вольтаж батареи

    >>> droid.batteryGetVoltage().result
    0


.. py:method:: batteryStartMonitoring()

    запуск мониторинга батареи

    >>> droid.batteryStopMonitoring().result
    None


.. py:method:: batteryStopMonitoring()

    останавливает мониторинг

    >>> droid.batteryStopMonitoring().result
    None


.. py:method:: readBatteryData()

    возвращает данные о батареи

    >>> droid.readBatteryData().result
    {
        u'status': 2, 
        u'temperature': 0, 
        u'level': 50, 
        u'battery_present': True, 
        u'plugged': 1, 
        u'health': 2, 
        u'voltage': 0, 
        u'technology': u'Li-ion'
    }