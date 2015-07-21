Location
========


.. py:method:: geocode(double latitude, double longitude[ , int maxResults=1])

    список адресов по геокоду


.. py:method:: getLastKnownLocation()

    возвращает последнюю известную позицию


.. py:method:: locationProviderEnabled(str provider)

    гпс устройство включено


.. py:method:: locationProviders()

    возвращает доступные гпс устройства


.. py:method:: readLocation()

    возвращает данные с гпс устройства


.. py:method:: startLocating([int minDistance=60000 ms, int minUpdateDistance=30 m])

    включает гпс учтройство, возбуждает "location" events.


.. py:method:: stopLocating()

    выключает гпс устройство