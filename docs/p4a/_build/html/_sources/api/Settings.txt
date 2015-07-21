Settings
========


.. py:method:: checkAirplaneMode()

    возвращает статус режима авиа


.. py:method:: checkRingerSilentMode()

    возвращает статус режима звука


.. py:method:: checkScreenOn()

    возвращает статус активности экрана


.. py:method:: getMaxMediaVolume()

    возвращает максимальное значение громкости медиа


.. py:method:: getMaxRingerVolume()

    возвращает максимальное значение уровня громкости звонка


.. py:method:: getMediaVolume()

    возвращает текущее значение громкости медиа


.. py:method:: getRingerVolume()

    вохзвращает текущий уровень громкости


.. py:method:: getScreenBrightness()

    возвращает текущий уровень подсветки от 0 до 255


.. py:method:: getScreenTimeout()

    возвращает время активности экрана


.. py:method:: getVibrateMode([bool ringer])

    провекра вибрации для звонка или для сообщений


.. py:method:: setMediaVolume(int volume)

    задает уровень громкости для медии


.. py:method:: setRingerVolume(int volume)
    
    задает уровень громкости для звонков


.. py:method:: setScreenBrightness(int value)

    задает уровень подсветки экрана в значение от 0 до 255


.. py:method:: setScreenTimeout(int value)

    задает время активности экрана в миллисекундах


.. py:method:: toggleAirplaneMode([bool enabled])

    включает или выключает режим авиа


.. py:method:: toggleRingerSilentMode([bool enabled])

    включает или выключает бесшумный режим для громкости


.. py:method:: toggleVibrateMode([bool enabled, bool ringer])

    включает или выключает вибрацию для звонков или для оповещений