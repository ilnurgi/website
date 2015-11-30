Sensors
=======

.. js:class:: Sensor

    :js:func:`CreateSensor`


    .. js:function:: SetMinChange()

        .. code-block:: js
            
            sns.SetMinChange(0);


    .. js:function:: SetOnChange(callback)

        Обработчик изменения состояния сенсора

        * для акселерометра в обработчик передаются 4 параметра - x, y, z, time

        * для gps - azimuth, pitch, roll, time

        * для освещенности - lux


    .. js:function:: Start()

        Запускает/включает сенсор

        .. code-block:: js
            
            sns.Start()