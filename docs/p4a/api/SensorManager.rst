SensorManager
=============

.. py:method:: readSensors()

    возвращает данные о сенсорах


.. py:method:: sensorsGetAccuracy()

    возвращает данные о сенсорах позиции


.. py:method:: sensorsGetLight()

    возвращает данные о сенсорах света


.. py:method:: sensorsReadAccelerometer()

    возвращает данные о акселерометре


.. py:method:: sensorsReadMagnetometer()

    возвращает данные о магнетометре


.. py:method:: sensorsReadOrientation()

    возвращает данные о ориентации


.. py:method:: startSensingThreshold(int sensorNumber, int threshold, int axis)

    :param int sensorNumber: 1 = Orientation, 2 = Accelerometer, 3 = Magnetometer, 4 = Light
    :param int axis: 0 = No axis, 1 = X, 2 = Y, 3 = X+Y, 4 = Z, 5= X+Z, 6 = Y+Z, 7 = X+Y+Z

    начинает запись данных с сенсора


.. py:method:: startSensingTimed(int sensorNumber, int delayTime)

    :param int sensorNumber: 1 = All, 2 = Accelerometer, 3 = Magnetometer and 4 = Light

    запускает сенсоры


.. py:method:: stopSensing()

    останавливает работу сенсоров