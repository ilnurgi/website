IOIO
====

.. js:class:: IOIO

    :js:func:`CreateIOIO`

    .. js:function:: Release()  

    .. js:function:: IsConnected()  

    .. js:function:: CheckConnection()  

    .. js:function:: SetOnConnect( p1 )     

    .. js:function:: SetOnError( p1 )   

    .. js:function:: CreateDigitalOutput( p1,p2,p3 )    

    .. js:function:: CreateDigitalInput( p1,p2 )    

    .. js:function:: CreatePwmOutput( p1,p2,p3 )    

    .. js:function:: CreateAnalogInput( p1 )    

    .. js:function:: CreateUart( p1,p2,p3,p4,p5,p6 )    

    .. js:function:: CreatePulseInput( p1,p2,p3 )


.. js:class:: IOIOUart

    .. js:function:: Close()    

    .. js:function:: Write( p1 )    

    .. js:function:: SetOnReceive( p1 )     

    .. js:function:: SetSplitMode( p1,p2,p3 )   

    .. js:function:: SetTimeout( p1 )   

    .. js:function:: Clear() 


.. js:class:: IOIODigitalOutput

    .. js:function:: Close()   

    .. js:function:: Write( p1 )


.. js:class:: IOIODigitalInput

    .. js:function:: Close()    

    .. js:function:: Read()     

    .. js:function:: WatchForValue( p1 )    

    .. js:function:: SetOnValue( p1 ) 


.. js:class:: IOIOPwmOutput

    .. js:function:: Close()   

    .. js:function:: SetPulseWidth( p1 )   

    .. js:function:: SetDutyCycle( p1 ) 


.. js:class:: IOIOAnalogInput

    .. js:function:: Close()     
    
    .. js:function:: Read() { return parseFloat(prompt( obj.id, “IAI.Read(” )); }    
    
    .. js:function:: GetReference()  
    
    .. js:function:: GetVoltage() 
    