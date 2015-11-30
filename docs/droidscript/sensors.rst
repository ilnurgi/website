Sensors
=======

.. js:class:: Sensor

    :js:func:`CreateSensor`


    .. js:function:: GetNames()

        lists all the sensor information

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


    
    .. js:function:: GetAzimuth() 
    
    .. js:function:: GetHeight()  
    
    .. js:function:: GetPitch()   
    
    .. js:function:: GetRoll()    
    
    .. js:function:: GetType()    
    
    .. js:function:: GetValues()  
    
    .. js:function:: SetMaxRate( rate )   default 20ms
    
    .. js:function:: Stop()