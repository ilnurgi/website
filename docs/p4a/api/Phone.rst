Phone
=====


.. py:method:: checkNetworkRoaming()

    возвращае True если смарт находится в домашней зоне


.. py:method:: getCellLocation()

    возвращает текущую информацию


.. py:method:: getDeviceId()

    возвращает уникальный идентификатор устройства, IMEI для GSM, MEID для CDMA или null


.. py:method:: getDeviceSoftwareVersion()

    возвращает версию ПО 


.. py:method:: getLine1Number()

    возвращает номер смарта для 1 линии


.. py:method:: getNeighboringCellInfo()

    возвращает информацию о сети


.. py:method:: getNetworkOperator()

    возвращает (MCC+MNC)


.. py:method:: getNetworkOperatorName()

    возвращает название оператора


.. py:method:: getNetworkType()

    возвращает тип сети


.. py:method:: getPhoneType()

    возвращает тип смарта


.. py:method:: getSimCountryIso()

    возвращает код страны в формате ISO


.. py:method:: getSimOperator()

    возвращает MCC+MNC (mobile country code + mobile network code)


.. py:method:: getSimOperatorName()

    возвращает имя опретаора сим


.. py:method:: getSimSerialNumber()

    возвращает номер SIM


.. py:method:: getSimState()

    возвращает статус симкарты


.. py:method:: getSubscriberId()

    возвращает уникальный ID


.. py:method:: getVoiceMailAlphaTag()

    возвращает номер почтового сервера 


.. py:method:: getVoiceMailNumber()

    возвращает номер почтового сервера


.. py:method:: phoneCall(str uri)

    набирает номер абонента


.. py:method:: phoneCallNumber(str phoneNumber)

    набирает номер абонента


.. py:method:: phoneDial(str uri)

    набирает номер абонента


.. py:method:: phoneDialNumber(str phoneNumber)

    набирает номер абонента


.. py:method:: readPhoneState()

    возвращает текущее состояние аппарата


.. py:method:: startTrackingPhoneState()

    запускает мониторинг состояния аппарата


.. py:method:: stopTrackingPhoneState()

    останавливает мониторинг состояния смарта